from .base_scraper import BaseScraper

class ECSScraper(BaseScraper):
    def __init__(self):
        super().__init__("ECS", "https://shopecs.com/collections/sale")
