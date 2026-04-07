from .base_scraper import BaseScraper

class CharcoalScraper(BaseScraper):
    def __init__(self):
        super().__init__("Charcoal", "https://charcoal.com.pk/collections/sale")
