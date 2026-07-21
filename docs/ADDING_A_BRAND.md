# Adding or maintaining a brand scraper

## Add a brand

1. Create `scraper/brands/<brand_name>.py`.
2. Implement a scraper class that returns a list of normalized product dictionaries.
3. Prefer inheriting from `BaseScraper` when the source follows common Shopify or HTML patterns.
4. Import and add an instance of the class to the `scrapers` list in `scraper/main.py`.
5. Add a matching filter button in `index.html` if the brand should be directly selectable in the dashboard.
6. Run `python scraper/main.py` locally and check `data.js` before committing.

## Minimum product fields

Every scraper should provide:

- `brand`
- `title`
- `original_price`
- `sale_price`
- `discount_percentage`
- `image_url`
- `url`
- `scraped_at`

## Guidelines

- Use reasonable request timeouts and rely on the shared request headers where possible.
- Do not bypass access controls, log in to sites, or evade rate limits.
- Keep parsing rules narrow and fail safely when expected markup is absent.
- Confirm that product URLs are absolute and image URLs are usable by the public dashboard.
- Treat source websites as authoritative; the tracker should link users back to the source rather than presenting its data as guaranteed current.

## When a scraper stops working

Retailer markup changes frequently. Start by checking the source URL and inspecting the current page structure. Update only the affected scraper, test it locally, and verify that the generated output still matches the data contract in [Architecture](ARCHITECTURE.md).
