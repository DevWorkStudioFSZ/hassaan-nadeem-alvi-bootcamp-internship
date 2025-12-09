# Google Maps Reviews Scraper (Selenium + Undetected ChromeDriver)

This script automatically scrolls through the reviews section of a Google Maps location and extracts the text from each review.  
It uses **Selenium**, **undetected-chromedriver**, and a scrolling loop to load and expand all available reviews before saving them into a CSV file. **This project was done for coding practice and learning purposes only, no reviews were saved or redistributed anywhere**

---

## 📌 What This Script Does

- Opens a Google Maps place page  
- Finds the reviews sidebar  
- Continuously scrolls through the panel  
- Expands “See more” buttons for long reviews  
- Collects each review's text  
- Saves the results to a CSV file using pandas  

---

## 📍 Target Example

The current script scrapes reviews from:

Joyland, Pakistan (Google Maps)


You can replace the URL at the top of the script with any other Google Maps place link.

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install selenium undetected-chromedriver pandas

▶️ How to Use

    Replace the Google Maps URL inside the script if needed.

    Run the Python file:

python your_script_name.py

    The script will:

        Launch Chrome

        Load the review panel

        Scroll until at least 50 unique reviews are collected

        Save them to:

joyland_google_maps_reviews.csv

    Press Enter when prompted to exit and close the browser.

📝 Output

The generated CSV contains one column:

Review

Each row contains the text of one Google Maps user review.
🔄 Customizing

You can modify:

    The target URL

    The number of reviews to collect

    The CSV output filename

    The scrolling delay and behavior

⚠️ Notes

    Google Maps loads reviews dynamically, so Selenium is required.

    Using undetected-chromedriver helps avoid Google’s bot detection.

    Heavy scrolling may take some time depending on the location’s review count.

📜 License

Free to use, modify, and learn from.
