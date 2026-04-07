from .base_scraper import BaseScraper

class HushPuppiesScraper(BaseScraper):
    def __init__(self):
        super().__init__("Hush Puppies", "https://hushpuppies.com.pk/collections/sale")
