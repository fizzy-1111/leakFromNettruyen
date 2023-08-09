from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Path to your Chrome WebDriver executable
chrome_driver_path = "/path/to/chromedriver"

# URL to fetch
url = "https://www.nettruyenmax.com/truyen-tranh/ijimeru-aitsu-ga-waruinoka-ijimerareta-boku-ga-waruinoka"

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

# Fetch the URL
driver.get(url)

# Get the page source
page_source = driver.page_source

# Close the WebDriver
driver.quit()

# Write the page source to a text file
output_file = "fetched_content.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(page_source)

print(f"Page source written to '{output_file}'")
