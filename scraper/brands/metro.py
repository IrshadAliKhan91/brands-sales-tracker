from .base_scraper import BaseScraper

class MetroShoesScraper(BaseScraper):
    def __init__(self):
        super().__init__("Metro Shoes", "https://www.metroshoes.com.pk/collections/sale")
