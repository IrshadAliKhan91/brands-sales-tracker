Brands Sales Tracker

[![Automated Sales Scraper](https://github.com/IrshadAliKhan91/brands-sales-tracker/actions/workflows/scrape.yml/badge.svg)](https://github.com/IrshadAliKhan91/brands-sales-tracker/actions/workflows/scrape.yml)

A static deal-discovery dashboard that tracks discounted products from dozens of fashion, footwear, and lifestyle brands. A scheduled GitHub Actions workflow runs the Python scraper daily, refreshes the tracked product data, and updates the live dashboard.

**Live dashboard:** [irshadalikhan91.github.io/brands-sales-tracker](https://irshadalikhan91.github.io/brands-sales-tracker/)

## What it does

- Collects sale products from supported brand websites
- Extracts product title, current price, original price, calculated discount, image, and source URL
- Filters duplicate listings before publishing the dataset
- Generates a browser-ready JavaScript data file for the dashboard
- Provides a searchable dashboard with brand filters and direct links to source products
- Refreshes the public dataset automatically through GitHub Actions

## How the automation works

```text
Daily GitHub Actions run
  -> Python brand scrapers
  -> normalization and de-duplication
  -> data.js
  -> automated commit to main
  -> GitHub Pages serves the refreshed dashboard
```

The workflow is scheduled for **00:00 UTC daily** and can also be started manually from the repository's **Actions** tab.

## Project structure

```text
.github/workflows/scrape.yml     Scheduled scraper automation
scraper/main.py                  Orchestrates all brand scrapers and writes output
scraper/brands/                  Shared scraper logic and brand-specific implementations
index.html                       GitHub Pages dashboard
data.js                          Generated browser-ready product dataset
```

## Run locally

### Prerequisites

- Python 3.10 or newer
- `pip`

### Install and scrape

```bash
git clone https://github.com/IrshadAliKhan91/brands-sales-tracker.git
cd brands-sales-tracker
python -m pip install -r requirements.txt
python scraper/main.py
```

### View the dashboard

Run a local static server from the repository root:

```bash
python -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000). On Windows, `start_dashboard.bat` performs the same step.

## Data notes and limitations

- Prices, stock, and discounts can change after a scrape. Always confirm details on the retailer's website before purchasing.
- A scraper can return no products when a source website changes its markup, rate limits requests, or has no qualifying sale items.
- The tracker keeps items with a calculated discount of at least 5% when enough price information is available.
- This project is not affiliated with, endorsed by, or operated by the brands represented in the dataset. Brand names, images, and product links belong to their respective owners.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Adding or maintaining a brand scraper](docs/ADDING_A_BRAND.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

## License

The source code is available under the [MIT License](LICENSE). Third-party brand names, images, product data, and website content are not covered by this license.
