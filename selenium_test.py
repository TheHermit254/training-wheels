from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

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

    # Find an element by ID and click it (Example using a sample ID, replace with actual)
    example_id = "more-information"
    element = driver.find_element(By.ID, example_id)
    print(f"Found element with ID {example_id}")
    element.click()
    print(f"Clicked element with ID {example_id}")

    # Send keys to an input field (Example using a sample name, replace with actual)
    input_name = "q"
    input_field = driver.find_element(By.NAME, input_name)
    input_text = "Selenium"
    input_field.send_keys(input_text + Keys.RETURN)
    print(f"Sent keys '{input_text}' to input field with name {input_name}")

    # Wait for an element to be present
    result_id = "result"
    wait = WebDriverWait(driver, 10)
    result = wait.until(EC.presence_of_element_located((By.ID, result_id)))
    print(f"Found result element with ID {result_id}")

    # Execute JavaScript
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

    # Mouse hover over an element (Example using a sample ID, replace with actual)
    hover_element_id = "hover-element"
    hover_element = driver.find_element(By.ID, hover_element_id)
    action = ActionChains(driver)
    action.move_to_element(hover_element).perform()
    print(f"Hovered over element with ID {hover_element_id}")

    # Drag and drop (Example using sample IDs, replace with actual)
    source_id = "drag-source"
    target_id = "drag-target"
    source_element = driver.find_element(By.ID, source_id)
    target_element = driver.find_element(By.ID, target_id)
    action.drag_and_drop(source_element, target_element).perform()
    print(f"Dragged element with ID {source_id} to element with ID {target_id}")

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
