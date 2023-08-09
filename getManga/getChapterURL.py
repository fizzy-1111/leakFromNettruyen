import re 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Read HTML content from file
chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
with open('fetched_content.txt', encoding='utf-8') as f:
  html = f.read()
  
def get_chapter_urls(html):
  pattern = re.compile(r'"url":"(https://www\.nettruyenmax\.com/[^"]+?)"')
  return pattern.findall(html)

def get_image_urls(html):
  pattern = re.compile(r'//[^"]+?\.jpg\?data=net"') 
  return pattern.findall(html)

urls = get_chapter_urls(html)
downloaded_urls = set()
for i, url in enumerate(urls):
  driver.get(url)
  html = driver.page_source
  
  image_urls = get_image_urls(html)
  
  output_file = f"chapter{i+1}_images.txt"
  with open(output_file, "a") as f:
    
    for url in image_urls:
      
      # Check if URL already downloaded
      if url not in downloaded_urls:
        f.write(url + "\n")
        downloaded_urls.add(url)
      
driver.quit()