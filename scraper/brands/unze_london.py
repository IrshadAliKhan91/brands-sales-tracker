from .base_scraper import BaseScraper

class UnzeLondonScraper(BaseScraper):
    def __init__(self):
        super().__init__("Unze London", "https://www.unze.com.pk/collections/sale")
