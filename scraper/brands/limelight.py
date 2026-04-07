from .base_scraper import BaseScraper

class LimelightScraper(BaseScraper):
    def __init__(self):
        super().__init__("Limelight", "https://www.limelight.pk/collections/sale")
