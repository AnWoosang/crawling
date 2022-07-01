import selenium
from selenium import webdriver as wd
import time
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from itertools import repeat
import datetime

def get_content(rank ,driv):
    contents = {}

    date_format = '%Y.%m.%d'
    html = driver.page_source
    soup = bs(html, 'html.parser')
    content = soup.find_all('dd')
    contents["rank"] = rank
    contents["song_name"] = ' '.join(soup.find('div', class_='song_name').get_text().split()[1:])
    contents["artist"] = driver.find_element(by='xpath', value='//*[@class="info"]/div[2]').text
    contents["likes"] = soup.find('span', id="d_like_count").get_text()
    contents["album"] = content[0].get_text()
    contents["released"] = datetime.datetime.strptime(content[1].get_text(), date_format)
    contents["genre"] = content[2].get_text()

    return contents

driver = wd.Chrome('C:/users/dntkd/Desktop/usang/adsl/melon/crawling/crawl/chromedriver.exe')
driver.maximize_window()

url = 'https://www.melon.com/chart/index.htm'
driver.get(url)

driver.find_element(by='xpath', value='//*[@class="chart_finder"]/button/span').click()
time.sleep(1)
driver.find_element(by='xpath', value='//*[@title="주간차트 상세찾기를 시작합니다."]').click()
time.sleep(1)

# path = '//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[2]/span/label'
# driver.find_element(by='xpath', value=path).click()
# path = '//*[@id="d_chart_search"]/div/div/div[1]/div[2]/ul/li[2]/span/label'

path_years = '//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li['
path_year = '//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li['
path_month = '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li['
path_weeks = '//*[@id="d_chart_search"]/div/div/div[4]/div[1]/ul/li['
path_genre = '//*[@id="d_chart_search"]/div/div/div[last()]/div[1]/ul/li[1]/span/label'
path_end = ']/span/label'

last_years = '//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[last()]/span/label'
last_year = '//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[last()]/span/label'
last_month = '//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[last()]/span/label'
last_weeks = '//*[@id="d_chart_search"]/div/div/div[4]/div[1]/ul/li[last()]/span/label'

chart_list_obj_s = '//*[@id="chartListObj"]/tr['
chart_list_obj_e = ']/td[4]/div/a/span'

i = 1
# 연대선택
while(1):
    time.sleep(0.1)
    v1 = path_years+str(i)+path_end
    driver.find_element(by='xpath', value=v1).click()
    
    j = 1
    # 연도선택
    while(1):
        time.sleep(0.3)
        v2 = path_year+str(j)+path_end
        driver.find_element(by='xpath', value=v2).click()
        
        # 월간선택
        k = 1
        while(1):
            time.sleep(0.1)
            v3 = path_month+str(k)+path_end
            driver.find_element(by='xpath', value=v3).click()

            # 주간선택
            l = 1
            while(1):
                time.sleep(0.1)
                v4 = path_weeks+str(l)+path_end
                print(driver.find_element(by='xpath', value='//*[@id="serch_cnt"]/span[1]').text)
                driver.find_element(by='xpath', value=v4).click()

                # 장르종합
                time.sleep(0.1)
                driver.find_element(by='xpath', value=path_genre).click()

                time.sleep(0.5)
                driver.find_element(by='xpath', value='//*[@title="차트 상세 검색"]').click()
                for x in range(1, 51):
                    time.sleep(1.0)
                    temp = chart_list_obj_s + str(x) + chart_list_obj_e
                    driver.find_element(by='xpath', value=temp).click() 
                    print(get_content(x, driver))
                    driver.back()
                
                # 51-100위 클릭
                driver.find_element(by='xpath', value='//*[@class="paginate chart_page"]/span/a').click()

                for x in range(51, 101):
                    time.sleep(0.5)
                    temp = chart_list_obj_s + str(x) + chart_list_obj_e
                    driver.find_element(by='xpath', value=temp).click()
                    print(get_content(x, driver))
                    driver.back()

                    

                if(driver.find_element(by='xpath', value=v4) == driver.find_element(by='xpath', value=last_weeks)):
                    break
                l+=1

            if(driver.find_element(by='xpath', value=v3) == driver.find_element(by='xpath', value=last_month)):
                break
            k+=1
            
        if(driver.find_element(by='xpath', value=v2) == driver.find_element(by='xpath', value=last_year)):
            break

        j+=1

    if(driver.find_element(by='xpath', value=v1) == driver.find_element(by='xpath', value=last_years)):
        break

    i+=1



time.sleep(5)
driver.quit()