import requests
from bs4 import BeautifulSoup

URL = "https://www.olx.com.pk/mobile-phones_c1453"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def scrape_main_page():
    response = requests.get(URL, headers=HEADERS)
    page = (response.text)
    if response.status_code != 200:
        print("Failed to fetch the page")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_data = []

    # Find all listing items
    listings = soup.find_all('li')
    for listing in listings:
        try:
            title_div = listing.find('div', attrs={'aria-label': 'Title'})
            price_div = listing.find('div', attrs={'aria-label': 'Price'})
            img_tag = listing.find('img')

            if title_div and price_div and img_tag:
                all_data.append({
                    "title": title_div.get_text(strip=True),
                    "price": price_div.get_text(strip=True),
                    "img": img_tag.get('src')
                })
        except Exception as e:
            continue

    return all_data

if __name__ == "__main__":
    data = scrape_main_page()
    for item in data:
        print(item)

