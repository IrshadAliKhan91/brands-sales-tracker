from .base_scraper import BaseScraper

class GulAhmedScraper(BaseScraper):
    def __init__(self):
        super().__init__("Gul Ahmed / Ideas", "https://www.gulahmedshop.com/collections/sale")
