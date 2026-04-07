from .base_scraper import BaseScraper

class FurorScraper(BaseScraper):
    def __init__(self):
        super().__init__("Furor", "https://furorjeans.com/collections/sale")
