import os

template = """from .base_scraper import BaseScraper

class {ClassPrefix}Scraper(BaseScraper):
    def __init__(self):
        super().__init__("{BrandName}", "{URL}")
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

for b in brands:
    filepath = f"scraper/brands/{b[0]}.py"
    print(f"Updating {filepath}")
    content = template.format(ClassPrefix=b[1], BrandName=b[2], URL=b[3])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
