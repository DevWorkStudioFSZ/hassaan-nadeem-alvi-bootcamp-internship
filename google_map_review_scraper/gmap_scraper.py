from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time, pandas as pd

chrome_options = uc.ChromeOptions()
driver = uc.Chrome(options=chrome_options)

driver.get("https://www.google.com/maps/place/Joyland/@33.5786254,73.077358,12.86z/data=!4m6!3m5!1s0x38dfecd312097875:0x4057399822bc2d29!8m2!3d33.5611826!4d73.0902946!16s%2Fg%2F11gnd3bw4d?entry=ttu&g_ep=EgoyMDI1MTExMi4wIKXMDSoASAFQAw%3D%3D")
wait = WebDriverWait(driver, 15)


sidebar = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//div[contains(@class,'m6QErb DxyBCb kA9KIf dS8AEf XiKgde')]")
))[0]

# Get initial scroll height of the element
last_height = driver.execute_script("return arguments[0].scrollHeight", sidebar)
all_reviews = []
while len(all_reviews)<50:
    SCROLL_PAUSE_TIME = 1.5
  

    # Scroll the element to the bottom
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)

    # Wait for new content to load
    time.sleep(SCROLL_PAUSE_TIME)

    # Expand truncated reviews
    more_buttons = sidebar.find_elements(By.XPATH, ".//button[contains(@aria-label,'See more')]")
    for btn in more_buttons:
        try:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(0.2)
        except:
            pass



    # Get newly loaded reviews
    reviews = sidebar.find_elements(By.XPATH, ".//span[contains(@class,'wiI7pd')]")
    
    # Append only new reviews
    for r in reviews:
        text = r.text
        if text not in all_reviews:
            all_reviews.append(text)

    # Get new scroll height
    new_height = driver.execute_script("return arguments[0].scrollHeight", sidebar)

    # Break if nothing new loaded
    if new_height == last_height:
        break

    last_height = new_height




# all_reviews is your collected list of reviews
df = pd.DataFrame(all_reviews, columns=["Review"])
df.to_csv("joyland_google_maps_reviews.csv", index=False, encoding="utf-8")

print("CSV saved successfully!")






 # sidebar = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@aria-label,'The Monal Rawalpindi')]")))
# SCROLL_PAUSE_TIME = 0.5  # wait 0.5 seconds after each scroll
# # Get initial scroll height
# last_height = driver.execute_script("return document.body.scrollHeight",sidebar)
# while True:
#     # Scroll to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)",sidebar)
#     # Wait for new content to load
#     time.sleep(SCROLL_PAUSE_TIME)
#     # Check if new content loaded by comparing scroll heights
#     new_height = driver.execute_script("return document.body.scrollHeight",sidebar)
#     if new_height == last_height:  # no new content
#         break
#     last_height = new_height

input("enter to quite")
driver.quit()
