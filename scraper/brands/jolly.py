from .base_scraper import BaseScraper

class JollyScraper(BaseScraper):
    def __init__(self):
        super().__init__("Jolly", "https://jolly.com.pk/collections/sale")
