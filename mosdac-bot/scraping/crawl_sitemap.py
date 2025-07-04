from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
import re

# List of URLs to scrape
URLS = [
    "https://mosdac.gov.in/insat-3dr",
    "https://mosdac.gov.in/insat-3dr-introduction",
    "https://mosdac.gov.in/insat-3dr-objectives",
    "https://mosdac.gov.in/insat-3dr-spacecraft",
    "https://mosdac.gov.in/insat-3dr-payloads",
    "https://mosdac.gov.in/insat-3d",
    "https://mosdac.gov.in/insat-3d-introduction",
    "https://mosdac.gov.in/insat-3d-objectives",
    "https://mosdac.gov.in/insat-3d-spacecraft",
    "https://mosdac.gov.in/insat-3d-payloads",
    "https://mosdac.gov.in/kalpana-1",
    "https://mosdac.gov.in/kalpana-1-introduction",
    "https://mosdac.gov.in/kalpana-1-objectives",
    "https://mosdac.gov.in/kalpana-1-spacecraft",
    "https://mosdac.gov.in/kalpana-1-payloads","https://mosdac.gov.in/3d-volumetric-terls-dwrproduct",
"https://mosdac.gov.in/about-us",
"https://mosdac.gov.in/announcements",
"https://mosdac.gov.in/atlases",
"https://mosdac.gov.in/bayesian-based-mt-saphir-rainfall",
"https://mosdac.gov.in/calibration-reports",
"https://mosdac.gov.in/contact-us",
"https://mosdac.gov.in/copyright-policy",
"https://mosdac.gov.in/data-access-policy",
"https://mosdac.gov.in/data-quality",
"https://mosdac.gov.in/docs/STQC.pdf",
"https://mosdac.gov.in/faq-page",
"https://mosdac.gov.in/gallery/index.html%3F%26prod%3D3SIMG_%2A_L1B_STD_IR1_V%2A.jpg",
"https://mosdac.gov.in/gallery/index.html?&prod=3SIMG_%2A_L1B_STD_IR1_V%2A.jpg",
"https://mosdac.gov.in/global-ocean-surface-current",
"https://mosdac.gov.in/gps-derived-integrated-water-vapour",
"https://mosdac.gov.in/gsmap-isro-rain",
"https://mosdac.gov.in/help",
"https://mosdac.gov.in/high-resolution-sea-surface-salinity",
"https://mosdac.gov.in/hyperlink-policy",
"https://mosdac.gov.in/imageshow",
"https://mosdac.gov.in/indian-mainland-coastal-product",
"https://mosdac.gov.in/inland-water-height",
"https://mosdac.gov.in/insat-3a",
"https://mosdac.gov.in/insat-3d",
"https://mosdac.gov.in/insat-3dr",
"https://mosdac.gov.in/insat-3ds",
"https://mosdac.gov.in/insitu",
"https://mosdac.gov.in/internal/afs-seac",
"https://mosdac.gov.in/internal/aws",
"https://mosdac.gov.in/internal/calval-data",
"https://mosdac.gov.in/internal/catalog-insitu",
"https://mosdac.gov.in/internal/catalog-radar",
"https://mosdac.gov.in/internal/catalog-satellite",
"https://mosdac.gov.in/internal/coldwave",
"https://mosdac.gov.in/internal/cyclone",
"https://mosdac.gov.in/internal/eddy",
"https://mosdac.gov.in/internal/energy",
"https://mosdac.gov.in/internal/event-heavyrain",
"https://mosdac.gov.in/internal/forecast-heavyrain",
"https://mosdac.gov.in/internal/forecast-menu",
"https://mosdac.gov.in/internal/gallery",
"https://mosdac.gov.in/internal/gallery/current",
"https://mosdac.gov.in/internal/gallery/dwr",
"https://mosdac.gov.in/internal/gallery/ocean",
"https://mosdac.gov.in/internal/gallery/weather",
"https://mosdac.gov.in/internal/heat-cold-wave",
"https://mosdac.gov.in/internal/lightning",
"https://mosdac.gov.in/internal/live",
"https://mosdac.gov.in/internal/logout",
"https://mosdac.gov.in/internal/monsoon",
"https://mosdac.gov.in/internal/nowcast-cloudburst",
"https://mosdac.gov.in/internal/nowcast-heavyrain",
"https://mosdac.gov.in/internal/ocean",
"https://mosdac.gov.in/internal/ocean-eye",
"https://mosdac.gov.in/internal/oilspill",
"https://mosdac.gov.in/internal/registration",
"https://mosdac.gov.in/internal/rip",
"https://mosdac.gov.in/internal/sea-state-forecast",
"https://mosdac.gov.in/internal/soil-wetness",
"https://mosdac.gov.in/internal/state",
"https://mosdac.gov.in/internal/uops",
"https://mosdac.gov.in/internal/urja",
"https://mosdac.gov.in/internal/varsha",
"https://mosdac.gov.in/internal/vayu",
"https://mosdac.gov.in/internal/weather",
"https://mosdac.gov.in/kalpana-1",
"https://mosdac.gov.in/megha-tropiques",
"https://mosdac.gov.in/meteosat8-cloud-properties",
"https://mosdac.gov.in/mosdac-feedback",
"https://mosdac.gov.in/node?qt-latest_products=0#qt-latest_products",
"https://mosdac.gov.in/node?qt-latest_products=1#qt-latest_products",
"https://mosdac.gov.in/node?qt-latest_products=2#qt-latest_products",
"https://mosdac.gov.in/node?qt-latest_products=3#qt-latest_products",
"https://mosdac.gov.in/node?qt-latest_products=4#qt-latest_products",
"https://mosdac.gov.in/node?qt-services_quicktab=0#qt-services_quicktab",
"https://mosdac.gov.in/node?qt-services_quicktab=1#qt-services_quicktab",
"https://mosdac.gov.in/node?qt-services_quicktab=2#qt-services_quicktab",
"https://mosdac.gov.in/node?qt-services_quicktab=3#qt-services_quicktab",
"https://mosdac.gov.in/node?qt-services_quicktab=4#qt-services_quicktab",
"https://mosdac.gov.in/node?qt-services_quicktab=5#qt-services_quicktab",
"https://mosdac.gov.in/ocean-subsurface",
"https://mosdac.gov.in/oceanic-eddies-detection",
"https://mosdac.gov.in/oceansat-2",
"https://mosdac.gov.in/oceansat-3",
"https://mosdac.gov.in/privacy-policy",
"https://mosdac.gov.in/river-discharge",
"https://mosdac.gov.in/rss-feed",
"https://mosdac.gov.in/rss.xml",
"https://mosdac.gov.in/saral-altika",
"https://mosdac.gov.in/scatsat-1",
"https://mosdac.gov.in/sea-ice-occurrence-probability",
"https://mosdac.gov.in/sitemap",
"https://mosdac.gov.in/sites/default/files/docs/INSAT_Product_Version_information_V01.pdf",
"https://mosdac.gov.in/sites/default/files/docs/Onset%20Prediction%202023.pdf",
"https://mosdac.gov.in/sites/default/files/docs/Onset%20Prediction%202024.pdf",
"https://mosdac.gov.in/sites/default/files/docs/sftp-mosdac_0.pdf",
"https://mosdac.gov.in/soil-moisture-0",
"https://mosdac.gov.in/terms-conditions",
"https://mosdac.gov.in/tools",
"https://mosdac.gov.in/validation-reports",
"https://mosdac.gov.in/wave-based-renewable-energy",
"https://mosdac.gov.in/weather-reports",
"https://mosdac.gov.in/website-policies"
]

# Output directory
os.makedirs("data/texts", exist_ok=True)

# Headless Chrome browser setup
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

# Safe filename from URL
def filename_from_url(url):
    return re.sub(r"https://mosdac.gov.in/", "", url).replace("/", "_") + ".txt"

# Scrape each URL
for url in URLS:
    print(f"⏳ Scraping: {url}")
    try:
        driver.get(url)
        time.sleep(5)  # Wait for JavaScript to load fully
        content = driver.find_element(By.TAG_NAME, "body").text
        filename = "data/texts/" + filename_from_url(url)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Saved: {filename}")
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")

driver.quit()
print("🚀 All pages scraped!")
