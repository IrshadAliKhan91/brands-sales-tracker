from .base_scraper import BaseScraper

class EdenrobeScraper(BaseScraper):
    def __init__(self):
        super().__init__("Edenrobe", "https://edenrobe.com/collections/sale")
