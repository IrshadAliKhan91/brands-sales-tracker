from .base_scraper import BaseScraper

class ShaposhScraper(BaseScraper):
    def __init__(self):
        super().__init__("Shaposh", "https://shaposh.pk/collections/sale")
