import requests
from bs4 import BeautifulSoup

def get_product_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        # SAFE EXTRACTION (fallbacks included)
        title = soup.title.text if soup.title else "No Title"
        price = "N/A"

        # return clean dict
        return {
            "name": title.strip(),
            "price": price,
            "source": "Website",
            "link": url
        }

    except Exception as e:
        return {
            "name": "Error fetching",
            "price": "N/A",
            "source": "Error",
            "link": url
        }