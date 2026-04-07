from .base_scraper import BaseScraper

class NishatLinenScraper(BaseScraper):
    def __init__(self):
        super().__init__("Nishat Linen", "https://nishatlinen.com/collections/sale")
