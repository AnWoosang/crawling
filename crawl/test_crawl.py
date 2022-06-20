import selenium
from selenium import webdriver as wd
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from itertools import repeat

def get_content(driv):
    contents = {}

    html = driver.page_source
    soup = bs(html, 'html.parser')
    content = soup.find_all('dd')

    contents["song_name"] = ' '.join(soup.find('div', class_='song_name').get_text().split()[1:])
    contents["artist"] = driver.find_element(by='xpath', value='//*[@class="info"]/div[2]').text
    contents["likes"] = soup.find('span', id="d_like_count").get_text()
    contents["album"] = content[0].get_text()
    contents["released"] = content[1].get_text()
    contents["genre"] = content[2].get_text()

    return contents

driver = wd.Chrome('/home/woosang/crawl/chromedriver')
driver.maximize_window()

url = 'https://www.melon.com/song/detail.htm?songId=34215822'
driver.get(url)

print(get_content(driver))

# html = driver.page_source
# soup = bs(html, 'html.parser')

# song_name = ' '.join(soup.find('div', class_='song_name').get_text().split()[1:])
# artist = driver.find_element(by='xpath', value='//*[@class="info"]/div[2]').text
# print(artist)
# context = soup.find_all('dd')
# likes = soup.find('span', id="d_like_count").get_text()
# album = context[0].get_text()
# released = context[1].get_text()
# genre = context[2].get_text()

# print("곡명 : " + song_name)
# print("가수 : " + artist)
# print("앨범 : " + album)
# print("발매일 : " + released)
# print("장르 : " + genre)
# print("좋아요 : " + likes)


driver.quit()

# for i in range(len(title)):
#     print(title[i].get_text())
