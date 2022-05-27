import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
d = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
webpage = "https://www.doordash.com/store/panera-bread-wall-township-856347/"
d.get(webpage)
WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='sc-bdVaJa BIHAZ']")))
cont=d.find_element_by_xpath("//span[@class='sc-bdVaJa BIHAZ']")
ActionChains(d).move_to_element(cont).click(cont).perform()

restaurant=d.find_element_by_tag_name('h1').text
'''adress=d.find_element_by_xpath("/html/body/div[1]/main/div/div[1]/div[1]/div[1]/div[20]/div/div[2]/span[3]").get_attribute('textContent')'''
upper=d.find_elements_by_xpath("//span[@class='sc-bdVaJa szuww']")
texts=[]
for up in upper:
    texts.append(up.text)
r1=texts[0]
r2=texts[1]
r3=texts[2]
r4=texts[3]
tag=d.find_element_by_xpath('/html/body/div[1]/main/div/div[1]/div[1]/div[1]/header/div[2]/div[1]/div[1]/span').text
cv=d.find_element_by_tag_name("img").get_attribute("src")
logo=d.find_element_by_xpath("//img[@loading='eager']").get_attribute("src")

import json as js
fob=open('panara1.json', 'r')
fob=fob.read()
file=js.loads(fob)


Data={
"restaurant_name": restaurant,
"clean_restaurant_name": restaurant,
 
"phone_number": " ",
"delivery_fee": " ",
"pickup_fee": "",
"rating_count": r2,
"rating_value": r1,
"offers": "",
"disclaimer": "",
"price_indicators": r4,
"pickup": "",
"catering": "",
"newly_added": "false",
"merchant_url_path": webpage,
"fulfills_own_deliveries": "",
"Process_date": "",

"business_name":restaurant ,
"business_name_clean": restaurant,
"business_tag": tag,
"place_type": "Restaurant",
"description": "",
"cuisine_Type": "",
"num_ratings_display": "",
"delivery": "",
"group_order": "",
"is_convenience": "",
"store_carousel": "",
"cover_image": cv,
"logo": logo, 
'Menu': file}


with open('panara2.json', 'w') as fob:
    js.dump(Data, fob)









