from .base_scraper import BaseScraper

class MoiccianiScraper(BaseScraper):
    def __init__(self):
        super().__init__("Moicciani", "https://moicciani.com/collections/sale")
