# OLX Scraper (Flask + Switchable Engines)

This project scrapes mobile phone listings from **OLX Pakistan** and displays them in a simple Flask frontend.

The scraper engine is **pluggable** — switching between **BeautifulSoup** and **Selenium** requires changing only one import line in `app.py`.

---

## 🔧 How It Works

The Flask app calls one function:

scrape_main_page()


You choose which scraper powers that function.

In `app.py`:

```python
from bs4_main import scrape_main_page        # Use BeautifulSoup
# from selenium_main import scrape_main_page   # Use Selenium

Switch the import → switch the technology.
📂 Project Structure

project/
│── app.py
│── bs4_main.py
│── selenium_main.py
│── templates/
│     └── listing.html
│── README.md

🥗 BeautifulSoup Version

    Fast

    Lightweight

    Works when OLX serves HTML normally

    Scrapes using requests + bs4

🛰 Selenium Version

    Handles Javascript-rendered content

    Uses undetected_chromedriver

    More reliable but heavier

▶️ Run the App

python app.py

Visit:

http://127.0.0.1:5000/

🎯 Why This Structure?

    Frontend stays the same.

    Backend scraping logic is fully swappable.

    Good foundation for:

        Web scraping projects

        API conversion

        Automation dashboards

📜 License

Free for learning and experimentation.
