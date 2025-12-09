Twitter (X) Automation with Selenium

This Jupyter notebook automates Twitter (X) login, tweet reading, and reposting using Selenium and undetected-chromedriver.
Features

    Automated Login: Logs into Twitter (X) with credentials

    Tweet Extraction: Reads the first tweet from the timeline

    Auto-Posting: Reposts the extracted tweet

    Anti-Detection: Uses undetected-chromedriver to avoid bot detection

Requirements

    Python 3.7+

    Jupyter Notebook

    Selenium

    undetected-chromedriver

Installation
bash

pip install selenium undetected-chromedriver

Setup

    Update credentials in the notebook:

python

email = "your_email@example.com"
password = "your_password"

    Ensure Chrome is installed

Usage

Run cells in order:

    Initialize driver

    Navigate to login

    Enter credentials

    Extract tweet

    Repost tweet

Notes

    Uses explicit waits for element loading

    Includes anti-detection measures

    Ensure stable internet connection
