from .base_scraper import BaseScraper

class BataScraper(BaseScraper):
    def __init__(self):
        super().__init__("Bata", "https://www.bata.com.pk/collections/sale")
