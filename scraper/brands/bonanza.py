from .base_scraper import BaseScraper

class BonanzaSatrangiScraper(BaseScraper):
    def __init__(self):
        super().__init__("Bonanza Satrangi", "https://www.bonanzasatrangi.com/collections/sale")
