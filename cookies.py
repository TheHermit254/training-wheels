import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize WebDriver
driver = webdriver.Chrome()

# Target website
url = "https://x.com/HackHubAfrica"

try:
    # Navigate to the target website
    driver.get(url)

    # Wait for the page to load completely
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Get cookies
    cookies = driver.get_cookies()

    # Save cookies to a JSON file
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file, indent=4)

    print("Cookies have been saved to cookies.json")

except TimeoutException:
    print("Timed out waiting for page to load")

finally:
    # Close the driver
    driver.quit()
