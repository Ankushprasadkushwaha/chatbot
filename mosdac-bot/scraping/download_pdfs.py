from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

url = "https://mosdac.gov.in/insat-3dr"
driver.get(url)
time.sleep(5)  # Wait for JS to load

text = driver.find_element(By.TAG_NAME, "body").text

os.makedirs("data/texts", exist_ok=True)
with open("data/texts/productdetails.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Saved content from productdetails page")
driver.quit()
