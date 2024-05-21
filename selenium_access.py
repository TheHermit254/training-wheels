from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

# Set up Chrome options
options = Options()
options.headless = False  # Set to True to run in headless mode

# Specify the path to chromedriver
service = Service("C:/Users/Administrator/Desktop/Projects/IP_INFO/chromedriver-win64/chromedriver.exe")  # Update the path if necessary

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open a URL
    driver.get("http://youtube.com")

    # Print the title of the page
    print(f"Title: {driver.title}")

    # Wait until the search box is present
    search_box_name = "search_query"
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, search_box_name)))

    # Send keys to the search box
    input_text = "Selenium WebDriver"
    search_box.send_keys(input_text + Keys.RETURN)
    print(f"Sent keys '{input_text}' to search box with name {search_box_name}")

    # Wait for search results to be present
    results_selector = "ytd-video-renderer"
    results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, results_selector)))
    print(f"Found {len(results)} results")

    # Execute JavaScript to get the page title
    script = "return document.title;"
    title = driver.execute_script(script)
    print(f"Executed script: {script} -> {title}")

    # Get cookies
    cookies = driver.get_cookies()
    print(f"Cookies: {cookies}")

    # Add a cookie
    cookie = {"name": "example_cookie", "value": "cookie_value"}
    driver.add_cookie(cookie)
    print(f"Added cookie: {cookie}")

    # Take a screenshot
    screenshot_path = "screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Saved screenshot to {screenshot_path}")

    # Mouse hover over an element (Example using a sample element, replace with actual)
    if results:
        hover_element = results[0]  # Just an example, hovering over the first result
        action = ActionChains(driver)
        action.move_to_element(hover_element).perform()
        print(f"Hovered over the first search result")

    # Drag and drop (Example using sample IDs, replace with actual)
    # Note: This example is generic as YouTube doesn't have drag and drop elements
    # source_id = "drag-source"
    # target_id = "drag-target"
    # source_element = driver.find_element(By.ID, source_id)
    # target_element = driver.find_element(By.ID, target_id)
    # action.drag_and_drop(source_element, target_element).perform()
    # print(f"Dragged element with ID {source_id} to element with ID {target_id}")

    # Handle alert (if any)
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("Accepted alert")
    except:
        print("No alert found")

finally:
    # Close the browser
    driver.quit()
    print("Closed the browser")
