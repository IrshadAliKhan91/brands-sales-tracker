from .base_scraper import BaseScraper

class UniworthScraper(BaseScraper):
    def __init__(self):
        super().__init__("Uniworth", "https://uniworthshop.com/collections/sale")
