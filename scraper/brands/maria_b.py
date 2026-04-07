from .base_scraper import BaseScraper

class MariaBScraper(BaseScraper):
    def __init__(self):
        super().__init__("Maria B.", "https://www.mariab.pk/collections/sale-view-all")
