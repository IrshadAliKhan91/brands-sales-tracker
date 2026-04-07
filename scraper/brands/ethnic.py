from .base_scraper import BaseScraper

class EthnicScraper(BaseScraper):
    def __init__(self):
        super().__init__("Ethnic", "https://pk.ethnc.com/collections/sale")
