# Contributing

Contributions are welcome, especially fixes for source-site changes and improvements to dashboard usability.

## Development setup

```bash
python -m pip install -r requirements.txt
python scraper/main.py
python -m http.server 8000
```

## Contribution guidelines

- Keep pull requests focused on one scraper, workflow, or dashboard improvement.
- Test the scraper locally before submitting changes.
- Do not commit secrets, private credentials, or `.env` files.
- Do not commit temporary Python caches or local virtual environments.
- Respect source websites: do not add code intended to bypass access restrictions or rate limits.
- Explain any generated-data changes in the pull request description.

## Reporting a broken source

Open an issue with the brand name, source URL, error/output, and the date you observed the issue. Avoid including personal information.
