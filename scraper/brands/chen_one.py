from .base_scraper import BaseScraper

class ChenOneScraper(BaseScraper):
    def __init__(self):
        super().__init__("Chen One", "https://chenone.com/collections/sale")
