import requests
from bs4 import BeautifulSoup
import os
import re

# Base domain
BASE_URL = "https://mosdac.gov.in/"

# Sitemap manually copied from page
PAGES = [
    "insat-3dr", "insat-3d", "kalpana-1", "insat-3a",
    "meghatropiques", "saral-altika", "oceansat-2", "oceansat-3",
    "insat-3ds", "scatsat-1"
]

os.makedirs("data/texts", exist_ok=True)

def clean_filename(url):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', url)

def extract_text(url_path):
    full_url = BASE_URL + url_path
    print(f"⏳ Scraping: {full_url}")
    try:
        res = requests.get(full_url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        text = soup.get_text(separator="\n", strip=True)
        
        filename = f"data/texts/{clean_filename(url_path)}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✅ Saved: {filename}")
    except Exception as e:
        print(f"❌ Failed to scrape {url_path}: {e}")

# Crawl all pages
for page in PAGES:
    extract_text(page)
