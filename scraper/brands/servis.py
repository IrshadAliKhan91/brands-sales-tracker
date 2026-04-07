from .base_scraper import BaseScraper

class ServisScraper(BaseScraper):
    def __init__(self):
        super().__init__("Servis", "https://servis.pk/collections/sale")
