from .base_scraper import BaseScraper

class AghaNoorScraper(BaseScraper):
    def __init__(self):
        super().__init__("Agha Noor", "https://aghanoorofficial.com/collections/sale")
