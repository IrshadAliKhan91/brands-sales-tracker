from brands.khaadi import KhaadiScraper
from brands.sapphire import SapphireScraper
from brands.j_jamshed import JunaidJamshedScraper
from brands.gul_ahmed import GulAhmedScraper
from brands.sana_safinaz import SanaSafinazScraper
from brands.alkaram_studio import AlkaramScraper
from brands.ethnic import EthnicScraper
from brands.outfitters import OutfittersScraper
from brands.maria_b import MariaBScraper
from brands.engine import EngineScraper
from brands.charcoal import CharcoalScraper
from brands.zellbury import ZellburyScraper
from brands.cougar import CougarScraper
from brands.one_brand import ONEScraper
from brands.bonanza import BonanzaSatrangiScraper
from brands.limelight import LimelightScraper
from brands.edenrobe import EdenrobeScraper
from brands.nishat import NishatLinenScraper
from brands.servis import ServisScraper
from brands.bata import BataScraper
from brands.borjan import BorjanScraper
from brands.hush_puppies import HushPuppiesScraper
from brands.ndure import NdureScraper
from brands.metro import MetroShoesScraper
from brands.diners import DinersScraper
from brands.uniworth import UniworthScraper
from brands.bareeze import BareezeScraper
from brands.unze_london import UnzeLondonScraper
from brands.ecs import ECSScraper
from brands.stylo import StyloScraper
from brands.lama import LamaScraper
from brands.generation import GenerationScraper
from brands.almirah import AlmirahScraper
from brands.chen_one import ChenOneScraper
from brands.furor import FurorScraper
from brands.moicciani import MoiccianiScraper
from brands.insignia import InsigniaScraper
from brands.agha_noor import AghaNoorScraper
from brands.rangja import RangjaScraper
from brands.taana_baana import TaanaBaanaScraper
from brands.shaposh import ShaposhScraper
from brands.clive import CliveScraper
from brands.jolly import JollyScraper
from brands.breakout import BreakoutScraper
from brands.beechtree import BeechtreeScraper
import json

def main():
    scrapers = [
        KhaadiScraper(),
        SapphireScraper(),
        JunaidJamshedScraper(),
        GulAhmedScraper(),
        SanaSafinazScraper(),
        AlkaramScraper(),
        EthnicScraper(),
        OutfittersScraper(),
        MariaBScraper(),
        EngineScraper(),
        CharcoalScraper(),
        ZellburyScraper(),
        CougarScraper(),
        ONEScraper(),
        BonanzaSatrangiScraper(),
        LimelightScraper(),
        EdenrobeScraper(),
        NishatLinenScraper(),
        ServisScraper(),
        BataScraper(),
        BorjanScraper(),
        HushPuppiesScraper(),
        NdureScraper(),
        MetroShoesScraper(),
        DinersScraper(),
        UniworthScraper(),
        BareezeScraper(),
        UnzeLondonScraper(),
        ECSScraper(),
        StyloScraper(),
        LamaScraper(),
        GenerationScraper(),
        AlmirahScraper(),
        ChenOneScraper(),
        FurorScraper(),
        MoiccianiScraper(),
        InsigniaScraper(),
        AghaNoorScraper(),
        RangjaScraper(),
        TaanaBaanaScraper(),
        ShaposhScraper(),
        CliveScraper(),
        JollyScraper(),
        BreakoutScraper(),
        BeechtreeScraper(),
    ]
    
    all_products = []
    import time
    for scraper in scrapers:
        try:
            all_products.extend(scraper.scrape())
            time.sleep(2) # Small delay to be respectful
        except Exception as e:
            print(f"Error running scraper {scraper.__class__.__name__}: {e}")
    
    # Deduplication: Remove identical items (brand, title, sale_price, url)
    unique_products = []
    seen = set()
    
    # Suffixes to strip for better deduplication (mostly for Uniworth)
    fit_suffixes = [" - SF", " - RF", " Slim Fit", " Regular Fit", " Smart Fit", " Classic Fit"]
    
    for p in all_products:
        title = p.get('title', '')
        # Strip fit suffixes from title for deduplication key
        clean_title = title
        for suffix in fit_suffixes:
            if suffix in clean_title:
                clean_title = clean_title.split(suffix)[0].strip()
        
        # Sanitization & Normalize URL
        url_raw = p.get('url', '')
        if not url_raw.startswith('http'):
            if url_raw.startswith('//'):
                p['url'] = 'https:' + url_raw
            else:
                p['url'] = 'https://' + url_raw
            
        url = p.get('url', '').split('?')[0].rstrip('/')
        
        # Create a unique key.
        key = (p.get('brand'), clean_title, str(p.get('sale_price')), url)
        
        if key not in seen:
            seen.add(key)
            # We keep the original title/url in the actual data, just use clean versions for key
            unique_products.append(p)
    
    all_products = unique_products

    # Save browser-ready data alongside the static GitHub Pages dashboard.
    output_js = 'data.js'
    with open(output_js, 'w') as f:
        f.write("window.salesData = ")
        json.dump(all_products, f, indent=2)
        f.write(";")
    
    print(f"Successfully saved {len(all_products)} products to {output_js}")

if __name__ == "__main__":
    main()
