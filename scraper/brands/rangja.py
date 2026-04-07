from .base_scraper import BaseScraper

class RangjaScraper(BaseScraper):
    def __init__(self):
        super().__init__("Rangja", "https://myrangja.com/collections/sale")
