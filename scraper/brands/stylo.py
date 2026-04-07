from .base_scraper import BaseScraper

class StyloScraper(BaseScraper):
    def __init__(self):
        super().__init__("Stylo", "https://stylo.pk/collections/sale")
