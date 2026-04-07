from .base_scraper import BaseScraper

class SapphireScraper(BaseScraper):
    def __init__(self):
        super().__init__("Sapphire", "https://pk.sapphireonline.pk/collections/sale")
