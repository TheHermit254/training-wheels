import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_ip_info_no_screenshot(ip):  # Function name reflects the change
  # Specify the path to the chromedriver executable
  service = Service("C:/chromedriver-win64/chromedriver.exe")  # Update this path to your chromedriver location
  options = Options()
  options.headless = False  # Run in non-headless mode (visible browser)

  # Initialize the Chrome driver with the service and options
  driver = webdriver.Chrome(service=service, options=options)

  url = f"https://whatismyipaddress.com/ip/{ip}"
  driver.get(url)

  # Add a delay to ensure the page loads completely
  time.sleep(5)

  # No screenshot functionality removed here

  print("Page loaded. Press any key to close the browser.")
  input()  # Wait for user input before closing

  driver.quit()

if __name__ == "__main__":
  # Removed ip input as there's no screenshot
  # ip_address = input("Enter IP address: ")
  get_ip_info_no_screenshot("your_ip_address")  # Replace with actual IP or remove entirely
  print("Browser closed.")
