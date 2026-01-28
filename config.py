# Mobile.de Scraper Configuration
# Edit these values to customize your search

# Car make (17200 = Mercedes-Benz, 1900 = Audi, etc.)
MAKE_VALUE = "17200"

# Car model (126 = S-Class for Mercedes, etc.)
MODEL_VALUE = "126"

# Maximum mileage (50000, 100000, etc.)
MAX_MILEAGE = "50000"

# Purchase type ("purchase" or "leasing")
PURCHASE_TYPE = "purchase"

# Delays (in seconds)
PAGE_LOAD_DELAY = 3
PAGINATION_DELAY = 2
CONSENT_TIMEOUT = 15

# Output files
LINKS_FILE_PREFIX = "article_links"
OUTPUT_FILE = "car_details_output.csv"

# Chrome options (add more if needed)
CHROME_OPTIONS = [
    "--headless",
    "--no-sandbox", 
    "--disable-dev-shm-usage",
    "--disable-extensions",
    "--disable-gpu",
    "--disable-web-security",
    "--allow-running-insecure-content",
    "--disable-blink-features=AutomationControlled"
]

# User agent for Linux
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
