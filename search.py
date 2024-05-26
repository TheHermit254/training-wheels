from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Specify the path to chromedriver
service = Service("C:/chromedriver-win64/chromedriver.exe")  # Update the path if necessary
service.start()

# Set up Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Open YouTube
driver.get("https://www.youtube.com")

# Find the search box and enter the query
search_box = driver.find_element(By.CSS_SELECTOR, "input#search")
search_box.send_keys("Alice in Wonderland")
search_box.send_keys(Keys.RETURN)

# Wait for search results to load
time.sleep(3)

# Take screenshot of the search results
driver.save_screenshot("alice_in_wonderland_search_results.png")

# Close the WebDriver
driver.quit()
