from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver_path = "D:/Flask1/earth911-webscraper/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

url = "https://search.earth911.com/?what=Electronics&where=10001&list_filter=all&max_distance=100"
driver.get(url)

# Wait until at least one result-item loads
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "result-item"))
)

cards = driver.find_elements(By.CLASS_NAME, "result-item")[:3]
print(f"Found {len(cards)} facilities")

facilities = []

for card in cards:
    try:
        name = card.find_element(By.CLASS_NAME, "description").text
    except:
        name = "N/A"
    try:
        updated = "N/A"  # Not available on the page
    except:
        updated = "N/A"
    try:
        address = card.find_element(By.CLASS_NAME, "contact").text
    except:
        address = "N/A"
    try:
        materials = card.find_element(By.CLASS_NAME, "result-materials").text
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
print("✅ CSV saved successfully.")
