from .base_scraper import BaseScraper

class BeechtreeScraper(BaseScraper):
    def __init__(self):
        super().__init__("Beechtree", "https://beechtree.pk/collections/sale")
