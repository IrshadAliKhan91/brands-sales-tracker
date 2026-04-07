import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime

def calculate_discount(original, sale):
    if not original or original == "N/A" or not sale or sale == "N/A":
        return 0
    try:
        o = float(re.sub(r'[^\d.]', '', original))
        s = float(re.sub(r'[^\d.]', '', sale))
        if o > s and s > 0:
            return round(((o - s) / o) * 100)
    except:
        pass
    return 0

class KhaadiScraper:
    def __init__(self):
        self.url = "https://pk.khaadi.com/sale/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def scrape(self):
        print(f"Scraping Khaadi: {self.url}")
        response = requests.get(self.url, headers=self.headers)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        
        items = soup.select('.product-tile')
        for item in items:
            try:
                title_elem = item.select_one('.link.plpRedirectPdp h2')
                title = title_elem.text.strip() if title_elem else "N/A"

                original_price_elem = item.select_one('.price .strike-through .value')
                original_price = original_price_elem.text.strip() if original_price_elem else "N/A"

                sale_price_elem = item.select_one('.price .sales .value')
                sale_price = sale_price_elem.text.strip() if sale_price_elem else "N/A"

                image_elem = item.select_one('.product-tile img.tile-image')
                image_url = image_elem['src'] if image_elem else "N/A"
                
                link_elem = item.select_one('.link.plpRedirectPdp')
                link = "https://pk.khaadi.com" + link_elem['href'] if link_elem else "N/A"

                discount_pct = calculate_discount(original_price, sale_price)

                if title != "N/A" and discount_pct > 0:
                    products.append({
                        "brand": "Khaadi",
                        "title": title,
                        "original_price": original_price,
                        "sale_price": sale_price,
                        "discount_percentage": discount_pct,
                        "image_url": image_url,
                        "url": link,
                        "scraped_at": datetime.now().isoformat()
                    })
            except Exception as e:
                pass

        print(f"Found {len(products)} valid discounted items for Khaadi")
        return products
