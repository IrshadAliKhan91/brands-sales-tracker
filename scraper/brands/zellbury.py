from .base_scraper import BaseScraper

class ZellburyScraper(BaseScraper):
    def __init__(self):
        super().__init__("Zellbury", "https://www.zellbury.com/collections/sale")
