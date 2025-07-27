from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# Replace this with your actual path


driver_path = "D:/Flask1/earth911-webscraper/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


# Load the Earth911 search page with filters
url = "https://search.earth911.com/?what=Electronics&where=10001&list_filter=all&max_distance=100&family_id="
driver.get(url)

# Wait for content to load
time.sleep(5)

facilities = []

# Select first 3 results
cards = driver.find_elements(By.CLASS_NAME, 'location-item')[:3]

for card in cards:
    try:
        name = card.find_element(By.CLASS_NAME, 'location__name').text
    except:
        name = "N/A"
    try:
        updated = card.find_element(By.CLASS_NAME, 'location__updated').text
    except:
        updated = "N/A"
    try:
        address = card.find_element(By.CLASS_NAME, 'location__address').text
    except:
        address = "N/A"
    try:
        materials = card.find_element(By.CLASS_NAME, 'location__materials').text
    except:
        materials = "N/A"

    facilities.append({
        "business_name": name,
        "last_update_date": updated,
        "street_address": address,
        "materials_accepted": materials
    })

driver.quit()

# Save to CSV
df = pd.DataFrame(facilities)
df.to_csv("earth911_results.csv", index=False)
print("CSV saved as 'earth911_results.csv'")
