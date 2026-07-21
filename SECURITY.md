# Security Policy

## Scope

This project runs public product-data collection and a static dashboard. It does not require user accounts or store user data.

## Reporting a vulnerability

Do not post sensitive details in a public issue. Contact the repository owner privately through GitHub with a clear description and reproduction steps.

## Operational guidance

- Keep GitHub Actions permissions limited to the workflow's needs.
- Store any future credentials in GitHub Actions secrets, never in the repository.
- Review dependencies and source-site changes before expanding scraper behavior.
