from .base_scraper import BaseScraper

class SanaSafinazScraper(BaseScraper):
    def __init__(self):
        super().__init__("Sana Safinaz", "https://sanasafinaz.com/collections/sale")
