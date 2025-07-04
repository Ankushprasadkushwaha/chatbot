from bs4 import BeautifulSoup
import requests

BASE = "https://mosdac.gov.in/filebrowser/download"
res = requests.get(BASE)
soup = BeautifulSoup(res.text, "html.parser")
urls = set()

for a in soup.find_all("a", href=True):
    href = a['href']
    if href.startswith("/"):
        urls.add(BASE + href)
    elif href.startswith(BASE):
        urls.add(href)

with open("all_urls.txt", "w") as f:
    f.write("\n".join(sorted(urls)))
