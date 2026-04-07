from .base_scraper import BaseScraper

class NdureScraper(BaseScraper):
    def __init__(self):
        super().__init__("Ndure", "https://ndure.com/collections/sale")
