from .base_scraper import BaseScraper

class ONEScraper(BaseScraper):
    def __init__(self):
        super().__init__("ONE", "https://beoneshopone.com/collections/sale")
