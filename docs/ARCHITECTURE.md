# Architecture

## Components

| Component | Responsibility |
| --- | --- |
| `scraper/brands/base_scraper.py` | Shared HTTP, price parsing, discount calculation, and common HTML/Shopify extraction behavior |
| `scraper/brands/*.py` | Brand-specific source URLs and parsing rules |
| `scraper/main.py` | Runs every scraper, handles individual failures, de-duplicates products, and writes output data |
| `data.js` | Generated browser-ready dataset loaded by the root dashboard |
| `frontend/public/data/sales_data.json` | Generated JSON dataset for the alternate frontend |
| `index.html` | Static dashboard used by GitHub Pages |
| `.github/workflows/scrape.yml` | Scheduled automation and generated-data commit step |

## Data contract

Each published product is normalized to a record similar to:

```json
{
  "brand": "Example Brand",
  "title": "Example product",
  "original_price": "Rs. 5,000",
  "sale_price": "Rs. 3,500",
  "discount_percentage": 30,
  "image_url": "https://example.com/image.jpg",
  "url": "https://example.com/product",
  "tags": [],
  "product_type": "",
  "scraped_at": "2026-01-01T00:00:00"
}
```

The orchestrator removes duplicates using a normalized combination of brand, title, sale price, and canonical product URL.

## Scheduled run

The GitHub Actions workflow runs daily at `00:00 UTC` and also supports `workflow_dispatch` for manual runs. It installs the requirements, runs `scraper/main.py`, and commits the two generated data files when they change.

## Failure behavior

Scrapers run independently. If one source fails, the orchestrator logs the exception and continues with the remaining brands, allowing a partial refresh rather than failing the entire dataset.
