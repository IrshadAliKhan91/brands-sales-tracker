import os

template = """import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime

def calculate_discount(original, sale):
    if not original or original == "N/A" or not sale or sale == "N/A":
        return 0
    try:
        o = float(re.sub(r'[^\\d.]', '', str(original)))
        s = float(re.sub(r'[^\\d.]', '', str(sale)))
        if o > s and s > 0:
            return round(((o - s) / o) * 100)
    except:
        pass
    return 0

class {ClassPrefix}Scraper:
    def __init__(self):
        self.url = "{URL}"
        self.headers = {{
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }}

    def scrape(self):
        print(f"Scraping {BrandName}: {{self.url}}")
        products = []
        
        try:
            json_url = self.url.split('?')[0] + "/products.json?limit=250"
            resp = requests.get(json_url, headers=self.headers, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                if 'products' in data and len(data['products']) > 0:
                    for item in data['products']:
                        title = item.get('title', 'N/A')
                        handle = item.get('handle', '')
                        base_url = self.url.split('/collections')[0] if '/collections' in self.url else self.url
                        link = base_url + "/products/" + handle if handle else self.url
                        
                        image_url = "N/A"
                        if item.get('images') and len(item['images']) > 0:
                            image_url = item['images'][0].get('src', 'N/A')
                            
                        variants = item.get('variants', [])
                        if variants:
                            v = variants[0]
                            sale_price = v.get('price', 'N/A')
                            original_price = v.get('compare_at_price') or 'N/A'
                            
                            discount_pct = calculate_discount(original_price, sale_price)
                            # To be robust on missing sales, we keep anything with compare_at_price > price
                            if discount_pct > 0:
                                products.append({{
                                    "brand": "{BrandName}",
                                    "title": title,
                                    "original_price": f"Rs. {{original_price}}",
                                    "sale_price": f"Rs. {{sale_price}}",
                                    "discount_percentage": discount_pct,
                                    "image_url": image_url,
                                    "url": link,
                                    "scraped_at": datetime.now().isoformat()
                                }})
                    
                    if len(products) > 0:
                        print(f"Found {{len(products)}} discounted items for {BrandName} via JSON API")
                        return products
        except Exception as e:
            # We fail silently and return [] if the site is not standard Shopify 
            # In future iteration, specific html targets can be set.
            pass
            
        print(f"Found 0 items for {BrandName} (Missing shopify config or empty sale)")
        return products
"""

brands = [
    ("lama", "Lama", "Lama", "https://lamaretail.com/collections/sale"),
    ("generation", "Generation", "Generation", "https://generation.com.pk/collections/sale"),
    ("almirah", "Almirah", "Almirah", "https://almirah.com.pk/collections/sale"),
    ("chen_one", "ChenOne", "Chen One", "https://chenone.com/collections/sale"),
    ("furor", "Furor", "Furor", "https://furorjeans.com/collections/sale"),
    ("moicciani", "Moicciani", "Moicciani", "https://moicciani.com/collections/sale"),
    ("insignia", "Insignia", "Insignia", "https://insignia.pk/collections/sale"),
    ("agha_noor", "AghaNoor", "Agha Noor", "https://aghanoorofficial.com/collections/sale"),
    ("rangja", "Rangja", "Rangja", "https://myrangja.com/collections/sale"),
    ("taana_baana", "TaanaBaana", "Taana Baana", "https://taanabaana.pk/collections/sale"),
    ("shaposh", "Shaposh", "Shaposh", "https://shaposh.pk/collections/sale"),
    ("clive", "Clive", "Clive", "https://cliveshoes.com/collections/sale"),
    ("jolly", "Jolly", "Jolly", "https://jolly.com.pk/collections/sale"),
    ("breakout", "Breakout", "Breakout", "https://breakout.com.pk/collections/sale"),
    ("beechtree", "Beechtree", "Beechtree", "https://beechtree.pk/collections/sale")
]

os.makedirs('scraper/brands', exist_ok=True)

for b in brands:
    filepath = f"scraper/brands/{b[0]}.py"
    if not os.path.exists(filepath):
        print(f"Writing {filepath}")
        content = template.format(ClassPrefix=b[1], BrandName=b[2], URL=b[3])
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

