from .base_scraper import BaseScraper

class GenerationScraper(BaseScraper):
    def __init__(self):
        super().__init__("Generation", "https://generation.com.pk/collections/sale")
