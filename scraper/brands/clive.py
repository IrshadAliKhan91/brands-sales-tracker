from .base_scraper import BaseScraper

class CliveScraper(BaseScraper):
    def __init__(self):
        super().__init__("Clive", "https://cliveshoes.com/collections/sale")
