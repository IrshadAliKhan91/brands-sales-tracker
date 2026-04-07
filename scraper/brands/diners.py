from .base_scraper import BaseScraper

class DinersScraper(BaseScraper):
    def __init__(self):
        super().__init__("Diners", "https://diners.com.pk/collections/sale")
