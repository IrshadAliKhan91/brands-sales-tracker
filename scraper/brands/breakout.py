from .base_scraper import BaseScraper

class BreakoutScraper(BaseScraper):
    def __init__(self):
        super().__init__("Breakout", "https://breakout.com.pk/collections/sale")
