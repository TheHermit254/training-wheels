from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = Options()
options.headless = False  # Set to True to run in headless mode

# Specify the path to chromedriver
service = Service("C:/Users/Administrator/Desktop/Projects/IP_INFO/chromedriver-win64/chromedriver.exe")  # Update the path if necessary

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the target URL
    target_url = "http://youtube.com"  # Replace with the target website
    driver.get(target_url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Get and print all cookies
    cookies = driver.get_cookies()
    print("Cookies found on the page:")
    for cookie in cookies:
        print(f"Name: {cookie['name']}, Value: {cookie['value']}")

    # Get and print all elements with IDs
    print("\nElements with IDs found on the page:")
    elements_with_ids = driver.find_elements(By.CSS_SELECTOR, "[id]")
    for element in elements_with_ids:
        print(f"Tag: {element.tag_name}, ID: {element.get_attribute('id')}")

    # Get and print all elements with specific attributes
    attributes_to_find = ["class", "name", "type"]  # Add other attributes as needed
    for attribute in attributes_to_find:
        print(f"\nElements with {attribute} attribute:")
        elements_with_attribute = driver.find_elements(By.CSS_SELECTOR, f"[{attribute}]")
        for element in elements_with_attribute:
            print(f"Tag: {element.tag_name}, {attribute.capitalize()}: {element.get_attribute(attribute)}")

finally:
    # Close the browser
    driver.quit()
    print("Closed the browser")
