from .base_scraper import BaseScraper

class LamaScraper(BaseScraper):
    def __init__(self):
        super().__init__("Lama", "https://lamaretail.com/collections/sale")
