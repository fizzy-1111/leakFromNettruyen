import requests
import base64
from io import BytesIO
from PIL import Image
import time


headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
  'Cache-Control': 'max-age=0', 
#   'If-Modified-Since': 'Wed, 19 Jul 2023 01:46:00 GMT',
#   'If-None-Match': '"3ec442c5e2b9d91:0"',
  'Referer': 'https://www.nettruyenmax.com/',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'cross-site',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

with open('chapter2_images.txt') as f:
  urls = f.read().splitlines()

fixed_urls = []
for url in urls:
    fixed_url = "https:" + url.strip('"')
    if "//i115.ntcdntempv3.com" in fixed_url:
        fixed_urls.append(fixed_url)

# Now fixed_urls contains the valid HTTPS urls  

for i, url in enumerate(fixed_urls):
    response = requests.get(url, headers=headers)
    file_name = f'chapter2/image{i+1}.png'

    with open(file_name, 'wb') as f:   
        print("get image "+str(i))
        f.write(response.content)
# url="https://i115.ntcdntempv3.com/data/images/60939/1027615/001-837ef07.jpg?data=net"
# url2="https://i115.ntcdntempv3.com/data/images/60939/1027615/001-837ef07.jpg?data=net"
# response = requests.get(url, headers=headers) 
# print(type(response.content)) 
# image_data = response.content 
# # Write bytes to file 
# with open('image.png', 'wb') as f: 
#     f.write(image_data)
