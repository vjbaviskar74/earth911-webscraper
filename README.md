# Earth911 Recycling Facility Scraper

## 🔍 Overview
This Python script scrapes recycling facilities from [Earth911](https://search.earth911.com) based on:
- Material: Electronics
- Zip Code: 10001
- Radius: 100 miles

## 📄 Output
Generates a CSV file (`earth911_results.csv`) with:
- `business_name`
- `last_update_date`
- `street_address`
- `materials_accepted`

## ⚙️ Tools Used
- `Selenium`: Automates Chrome browser to scrape data
- `Pandas`: Formats and exports data as CSV

## 🧠 Logic
- Script loads Earth911's search page
- Waits 5 seconds for dynamic content
- Extracts the first 3 facilities from the search results
- Handles missing fields gracefully

## 📌 How to Run
1. Install ChromeDriver and update the path in the script
2. Install required packages:
   ```bash
   pip install selenium pandas
