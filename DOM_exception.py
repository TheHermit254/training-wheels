from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# Set up Chrome options
options = Options()
options.headless = True  # Set to False if you want to see the browser

# Specify the path to chromedriver
service = Service("C:/Users/Administrator/Desktop/Projects/IP_INFO/chromedriver-win64/chromedriver.exe")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open a URL
    driver.get("http://github.com")

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Get cookies
    cookies = driver.get_cookies()

    # Write cookies to a file
    with open("scraped_data.txt", "w") as file:
        file.write("Cookies found on the page:\n")
        for cookie in cookies:
            file.write(f"Name: {cookie['name']}, Value: {cookie['value']}\n")
        
        file.write("\nElements with IDs found on the page:\n")

        # Get all elements with an ID
        elements_with_ids = driver.find_elements(By.XPATH, "//*[@id]")

        for element in elements_with_ids:
            try:
                file.write(f"Tag: {element.tag_name}, ID: {element.get_attribute('id')}\n")
            except StaleElementReferenceException:
                # Re-locate the element and try again
                element_id = element.get_attribute('id')
                element = driver.find_element(By.ID, element_id)
                file.write(f"Tag: {element.tag_name}, ID: {element_id}\n")
                
        print("Results saved to scraped_data.txt")

finally:
    # Close the browser
    driver.quit()
    print("Closed the browser")
