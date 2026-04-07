from .base_scraper import BaseScraper

class BorjanScraper(BaseScraper):
    def __init__(self):
        super().__init__("Borjan", "https://www.borjan.com.pk/collections/sale")
