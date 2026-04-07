from .base_scraper import BaseScraper

class TaanaBaanaScraper(BaseScraper):
    def __init__(self):
        super().__init__("Taana Baana", "https://taanabaana.pk/collections/sale")
