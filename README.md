# Daraz Playwright Automation

A production-ready automation framework for Daraz.pk using Python, Playwright, and Pytest, following the Page Object Model (POM).

## Prerequisites
- Python 3.8+
- Node.js (for Playwright browser binaries)

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Browsers**
   ```bash
   playwright install chromium
   ```

## Running Tests

Run the tests with the following command:
```bash
pytest tests/test_daraz_search.py --headed
```

## Structure
- `pages/`: Page Object classes (Base, Home, Results, Product)
- `tests/`: Test scripts and configuration
- `requirements.txt`: Project dependencies
