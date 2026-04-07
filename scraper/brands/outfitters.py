from .base_scraper import BaseScraper

class OutfittersScraper(BaseScraper):
    def __init__(self):
        super().__init__("Outfitters", "https://outfitters.com.pk/collections/women-special-prices")
