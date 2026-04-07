from .base_scraper import BaseScraper

class CougarScraper(BaseScraper):
    def __init__(self):
        super().__init__("Cougar", "https://www.cougar.com.pk/collections/sale")
