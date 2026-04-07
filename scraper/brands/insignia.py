from .base_scraper import BaseScraper

class InsigniaScraper(BaseScraper):
    def __init__(self):
        super().__init__("Insignia", "https://insignia.pk/collections/sale")
