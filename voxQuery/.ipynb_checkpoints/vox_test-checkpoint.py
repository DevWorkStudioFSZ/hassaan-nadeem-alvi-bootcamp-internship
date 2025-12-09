from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://web.whatsapp.com")
    print(page.title())
    input("press enter to close")
    browser.close()
