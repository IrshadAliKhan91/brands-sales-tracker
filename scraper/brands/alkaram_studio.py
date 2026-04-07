from .base_scraper import BaseScraper

class AlkaramScraper(BaseScraper):
    def __init__(self):
        super().__init__("Alkaram Studio", "https://www.alkaramstudio.com/collections/sale")

    def get_items(self, soup):
        return soup.select('.product-item')
