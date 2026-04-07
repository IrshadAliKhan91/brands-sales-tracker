import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from urllib.parse import urlparse

class BaseScraper:
    def __init__(self, brand_name, sale_url):
        self.brand_name = brand_name
        self.url = sale_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
            "Upgrade-Insecure-Requests": "1"
        }

    def calculate_discount(self, original, sale):
        if original <= 0 or sale <= 0:
            return 0
        if original > sale:
            return round(((original - sale) / original) * 100)
        return 0

    def extract_prices(self, text):
        raw_numbers = re.findall(r'[\d,]+\.?\d*', text)
        prices = []
        for n in raw_numbers:
            try:
                val = float(n.replace(',', ''))
                if val >= 100:
                    prices.append(val)
            except:
                pass
        return sorted(list(set(prices)), reverse=True)

    def scrape_shopify_json(self):
        # Try multiple common Shopify JSON endpoints
        endpoints = [
            self.url.split('/collections')[0] + "/products.json?limit=250",
            self.url.rstrip('/') + ".json?limit=250",
            self.url.split('/collections')[0] + "/collections/all/products.json?limit=250"
        ]
        
        # Deduplicate endpoints
        endpoints = list(dict.fromkeys(endpoints))
        
        for json_url in endpoints:
            print(f"Trying Shopify JSON API for {self.brand_name}: {json_url}")
            try:
                r = requests.get(json_url, headers=self.headers, timeout=20)
                if r.status_code != 200: continue
                data = r.json()
                products = []
                for p in data.get('products', []):
                    # Filter for items on sale
                    # Check variants for price vs compare_at_price
                    for variant in p.get('variants', []):
                        original = float(variant.get('compare_at_price') or 0)
                        sale = float(variant.get('price') or 0)
                        
                        if original > sale and sale > 0:
                            discount = self.calculate_discount(original, sale)
                            if discount >= 5:
                                img = p.get('images', [{}])[0].get('src', '')
                                
                                # Extract tags and product type for better categorization
                                tags = [tag.lower() for tag in p.get('tags', [])]
                                product_type = p.get('product_type', '').lower()
                                
                                # Robust URL generation
                                parsed_url = urlparse(self.url)
                                base_domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
                                product_url = f"{base_domain}/products/{p.get('handle')}"
                                
                                products.append({
                                    "brand": self.brand_name,
                                    "title": p.get('title'),
                                    "original_price": f"Rs. {original:,.0f}",
                                    "sale_price": f"Rs. {sale:,.0f}",
                                    "discount_percentage": discount,
                                    "image_url": img,
                                    "url": product_url,
                                    "tags": tags,
                                    "product_type": product_type,
                                    "scraped_at": datetime.now().isoformat()
                                })
                                break # Only add product once
                if products:
                    return products
            except Exception as e:
                print(f"Shopify JSON error for {self.brand_name} at {json_url}: {e}")
        return []

    def scrape(self):
        # Prefer JSON API for Shopify sites if URL structure matches
        if "/collections/" in self.url or "/products/" in self.url:
            results = self.scrape_shopify_json()
            if results: 
                print(f"Found {len(results)} items via JSON API for {self.brand_name}")
                return results

        try:
            response = requests.get(self.url, headers=self.headers, timeout=20)
            if response.status_code != 200:
                print(f"Failed to load {self.brand_name}: status {response.status_code}")
                return []
        except Exception as e:
            print(f"Connection error for {self.brand_name}: {e}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        
        # This will be overridden or used with standard Shopify-like selectors
        items = self.get_items(soup)
        for item in items:
            try:
                data = self.parse_item(item)
                if data:
                    products.append(data)
            except Exception as e:
                pass

        print(f"Found {len(products)} valid discounted items for {self.brand_name}")
        return products

    def get_items(self, soup):
        return soup.select('.grid__item, .product-item')

    def parse_item(self, item):
        # Override this in specific brand scrapers if needed
        # Standard Shopify theme selectors as default
        title_elem = item.select_one('.full-unstyled-link, .card-title, .product-title')
        if not title_elem: return None
        
        title = title_elem.text.strip()
        link = title_elem.get('href', '')
        if link and not link.startswith('http'):
            parsed_url = urlparse(self.url)
            base_domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
            link = base_domain + (link if link.startswith('/') else '/' + link)

        price_elem = item.select_one('.price, .product-item-price')
        if not price_elem: return None
        
        prices = self.extract_prices(price_elem.text)
        
        original_price = 0
        sale_price = 0

        if len(prices) >= 2:
            original_price = prices[0]
            sale_price = prices[-1]
        else:
            # Look for specific selectors for regular vs sale
            reg = item.select_one('.price-item--regular, .price--compare-at, .old-price')
            sale = item.select_one('.price-item--sale, .price--highlight, .final-price')
            if reg and sale:
                p_reg = self.extract_prices(reg.text)
                p_sale = self.extract_prices(sale.text)
                if p_reg and p_sale:
                    original_price = p_reg[0]
                    sale_price = p_sale[0]
            elif len(prices) == 1 and "/sale" in self.url:
                # Fallback: if we only find 1 price on a sale page, we might be missing the original
                # but we can't calculate discount without it.
                return None

        if original_price <= 0 or sale_price <= 0:
            return None

        discount_pct = self.calculate_discount(original_price, sale_price)
        if discount_pct <= 0: return None

        # Filter out 0% or low discounts that might be mistakes
        if discount_pct < 5: return None

        img_elem = item.select_one('img.card-media, img.product-card__media, .card__media img, .product-item-photo img, img')
        if not img_elem: return None
        
        image_url = img_elem.get('data-src') or img_elem.get('src') or img_elem.get('srcset', '').split(' ')[0]
        if image_url and image_url.startswith('//'):
            image_url = "https:" + image_url
            
        if image_url == "N/A" or not image_url or image_url.startswith('data:image'):
            return None

        return {
            "brand": self.brand_name,
            "title": title,
            "original_price": f"Rs. {original_price:,.2f}".replace(".00", ""),
            "sale_price": f"Rs. {sale_price:,.2f}".replace(".00", ""),
            "discount_percentage": discount_pct,
            "image_url": image_url,
            "url": link,
            "tags": [], # HTML fallback doesn't easily expose tags
            "product_type": "", 
            "scraped_at": datetime.now().isoformat()
        }
