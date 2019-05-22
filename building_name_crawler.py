import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time

#Load buildings.json
with open('buildings.json') as data_file_building:    
    building_data = json.load(data_file_building)

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=996x1000')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('./chromedriver', options=options)
driver.implicitly_wait(3)
driver.get('http://map.snu.ac.kr/web/main.action')

#if you want en, able below code
driver.find_element_by_css_selector('#kor').click()


for building in building_data:
    #search
    driver.get('http://map.snu.ac.kr/web/main.action')
    driver.find_element_by_css_selector('#search_word').clear()
    driver.find_element_by_css_selector('#search_word').send_keys(building["building_no"])
    driver.find_element_by_css_selector('button.searchBtn').click()
    building["en_name"] = str(building["building_no"])+"DONG"
    for i in range(1, 1000):
        try:
            target = driver.find_element_by_css_selector('#add_category > .place:nth-child('+str(i)+') strong')
            target.location_once_scrolled_into_view
            target.click()
        except:
            break
        else:
            kr_name_html = driver.page_source
            kr_name_soup = BeautifulSoup(kr_name_html, 'html.parser')
            building_kr_name = kr_name_soup.select('#add_category > .place:nth-child('+str(i)+') strong')[0].text
            codePattern = re.compile('\([-\d]+[^-\d]+\)')
            codeMatch = codePattern.search(building_kr_name)
            code = ""
            if codeMatch:
                codePurePattern = re.compile('[-\d]+')
                codePureMatch = codePurePattern.search(codeMatch.group())
                code = codePureMatch.group()
            if str(building["building_no"]) == code:
                building["en_name"] = building_kr_name
                print(building_kr_name)
                break
driver.close ()

with open('buildings.json', 'w', encoding="utf-8") as make_file:
    json.dump(building_data, make_file, ensure_ascii=False, indent=4)

    
#driver.find_element_by_css_selector('#add_category > .place:nth-child(1) strong').click()
#driver.find_element_by_css_selector('#add_category > .place:nth-child(1) .clickPlace > a').click()

# req = requests.get(driver.current_url)
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
# infos = soup.select('div.asideCon')

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# infos = soup.select('.smallIcons:nth-child(1) > a')