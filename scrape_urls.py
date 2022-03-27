# NOTE: Thanks https://github.com/banhao for his script to scrape the urls(it was modified for my purposes).
# All the credits are given.
# Copyright notice will be included at the end of the script.
# This script will not be used as a commercial product. Just as a learning experience and useful personal tool.

# imports
import datetime
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from main import main

# config
url = sys.argv[1]
channel_id = url.split('/')[4]
chrome_options = Options()
driver = webdriver.Chrome("C://Development//chromedriver.exe", options=chrome_options)
driver.get(url)

time.sleep(5)
last_height = 0
height = driver.execute_script("return document.documentElement.scrollHeight")
dt = datetime.datetime.now().strftime("%Y%m%d%H%M")

# get the links
while True:
    if last_height == height:
        break

    last_height = height
    driver.execute_script(f"window.scrollTo(0, {str(height)});")
    time.sleep(2)
    height = driver.execute_script("return document.documentElement.scrollHeight")

user_data = driver.find_elements(by=By.XPATH, value='//*[@id="video-title"]')

# loop through data and write the links
for i in user_data:
    # get the link
    link = (i.get_attribute('href'))

    # write the links
    with open(f"links.list", "w") as file:
        if link:
            file.write(f"{link}\n")

# download the videos
main()


# Copyright (c) 2022 banhao
