from .base_scraper import BaseScraper

class AlmirahScraper(BaseScraper):
    def __init__(self):
        super().__init__("Almirah", "https://almirah.com.pk/collections/sale")
