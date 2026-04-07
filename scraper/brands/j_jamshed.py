import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime

def calculate_discount(original, sale):
    if original <= 0 or sale <= 0:
        return 0
    if original > sale:
        return round(((original - sale) / original) * 100)
    return 0

def extract_prices(text):
    raw_numbers = re.findall(r'[\d,]+\.?\d*', text)
    prices = []
    for n in raw_numbers:
        try:
            val = float(n.replace(',', ''))
            # Filter out percentages like 50 from 50% OFF, assuming no item sells for < Rs. 100
            if val >= 100:
                prices.append(val)
        except:
            pass
    prices = sorted(list(set(prices)), reverse=True)
    return prices

class JunaidJamshedScraper:
    def __init__(self):
        self.url = "https://www.junaidjamshed.com/sale.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def scrape(self):
        print(f"Scraping J.: {self.url}")
        response = requests.get(self.url, headers=self.headers)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        
        items = soup.select('.product-item')
        for item in items:
            try:
                title_elem = item.select_one('.product-item-link')
                if not title_elem: continue
                title = title_elem.text.strip()
                link = title_elem['href']

                # Use data attributes for more reliable extraction
                price_box = item.select_one('.price-box')
                if not price_box: continue

                # Look for data-price-amount for final and old price
                final_wrapper = price_box.select_one('[data-price-type="finalPrice"]')
                old_wrapper = price_box.select_one('[data-price-type="oldPrice"]')
                
                if final_wrapper and old_wrapper:
                    sale_price = float(final_wrapper.get('data-price-amount', 0))
                    original_price = float(old_wrapper.get('data-price-amount', 0))
                else:
                    # Fallback to regex extraction
                    prices = extract_prices(price_box.text)
                    if len(prices) >= 2:
                        original_price = prices[0]
                        sale_price = prices[-1]
                    else:
                        continue

                discount_pct = calculate_discount(original_price, sale_price)

                image_elem = item.select_one('img.product-image-photo')
                image_url = "N/A"
                if image_elem:
                    image_url = image_elem.get('data-src') or image_elem.get('src')
                    if image_url and "Loader.gif" in image_url and image_elem.has_attr('data-original'):
                        image_url = image_elem['data-original']

                if title and discount_pct > 0 and image_url != "N/A" and not image_url.startswith('data:image'):
                    products.append({
                        "brand": "J.",
                        "title": title,
                        "original_price": f"Rs. {original_price:,.2f}".replace(".00", ""),
                        "sale_price": f"Rs. {sale_price:,.2f}".replace(".00", ""),
                        "discount_percentage": discount_pct,
                        "image_url": image_url,
                        "url": link,
                        "scraped_at": datetime.now().isoformat()
                    })
            except Exception as e:
                pass

        print(f"Found {len(products)} valid discounted items for J.")
        return products
