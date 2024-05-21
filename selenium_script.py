from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = Options()
options.headless = True  # Run in headless mode

# Specify the path to chromedriver
service = Service("C:/Users/Administrator/Desktop/Projects/IP_INFO/chromedriver-win64/chromedriver.exe")  # Update the path

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open a URL
driver.get("http://github.com")

# Find an element by ID and click it
element = driver.find_element(By.ID, "example_id")
element.click()

# Send keys to an input field
input_field = driver.find_element(By.NAME, "q")
input_field.send_keys("Selenium" + Keys.RETURN)

# Wait for an element to be present
wait = WebDriverWait(driver, 10)
result = wait.until(EC.presence_of_element_located((By.ID, "result_id")))

# Take a screenshot
driver.save_screenshot("screenshot.png")

# Close the browser
driver.quit()
