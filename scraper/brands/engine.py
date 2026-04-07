from .base_scraper import BaseScraper

class EngineScraper(BaseScraper):
    def __init__(self):
        super().__init__("Engine", "https://engine.com.pk/collections/sale")
