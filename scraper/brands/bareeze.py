import requests
from bs4 import BeautifulSoup
from datetime import datetime

class BareezeScraper:
    def __init__(self):
        self.brand_name = "Bareeze"
        self.base_url = "https://bareeze.com"
        self.sale_url = "https://bareeze.com/sale"

    def scrape(self):
        print(f"Scraping {self.brand_name}...")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        try:
            response = requests.get(self.sale_url, headers=headers, timeout=30)
            if response.status_code != 200:
                print(f"Failed to fetch {self.brand_name}: {response.status_code}")
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.select('.singleProductCardContainer')
            
            products = []
            for item in items:
                try:
                    title_elem = item.select_one('.singleProductCardProductTitle')
                    title = title_elem.get_text(strip=True) if title_elem else "Breeeze Product"
                    
                    sale_price_elem = item.select_one('.singleProductCardSalePrice')
                    actual_price_elem = item.select_one('.singleProductCardActualPrice')
                    
                    if not sale_price_elem or not actual_price_elem:
                        continue
                        
                    sale_price_str = sale_price_elem.get_text(strip=True).replace('PKR', '').replace(',', '').strip()
                    actual_price_str = actual_price_elem.get_text(strip=True).replace('PKR', '').replace(',', '').strip()
                    
                    sale_price = float(sale_price_str)
                    actual_price = float(actual_price_str)
                    
                    link_elem = item.select_one('.singleProductCardProductBottom a')
                    link = self.base_url + link_elem['href'] if link_elem else self.sale_url
                    
                    img_elem = item.select_one('.carousel_container img')
                    image_url = img_elem['src'] if img_elem else ""
                    
                    discount = round(((actual_price - sale_price) / actual_price) * 100) if actual_price > 0 else 0
                    if title and sale_price:
                        products.append({
                            "brand": "Bareeze",
                            "title": title,
                            "original_price": f"PKR {int(actual_price):,}",
                            "sale_price": f"PKR {int(sale_price):,}",
                            "discount_percentage": discount,
                            "image_url": image_url,
                            "url": link,
                            "scraped_at": datetime.now().isoformat()
                        })
                except Exception as e:
                    print(f"Error parsing item for {self.brand_name}: {e}")
                    continue
            
            print(f"Successfully scraped {len(products)} items from {self.brand_name}")
            return products
        except Exception as e:
            print(f"Error scraping {self.brand_name}: {e}")
            return []

