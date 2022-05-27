import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


Data={}
Categories=[]


d = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
webpage = "https://www.doordash.com/store/panera-bread-wall-township-856347/"
d.get(webpage)
WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='sc-bdVaJa BIHAZ']")))
cont=d.find_element_by_xpath("//span[@class='sc-bdVaJa BIHAZ']")
ActionChains(d).move_to_element(cont).click(cont).perform()
d.find_element_by_xpath("//span[@class='sc-bdVaJa hoNTOb']").click()
path_indexs=range(4,19)
for path_index in path_indexs:
    path="/html/body/div[1]/main/div/div[1]/div[1]/div[1]/div[{}]".format(path_index)
    mains=d.find_element_by_xpath(path)
    title=mains.find_element_by_tag_name('h2').get_attribute('textContent')
    print(title)
    category={}
    item=[]
    submains=d.find_element_by_xpath(path).find_elements_by_tag_name("button")
    for submain in submains:
             try:
                submain.click()
                WebDriverWait(d, 20).until(EC.presence_of_element_located((By.XPATH,"//span[@class='sc-bdVaJa eSMcEc']")))
                meal=d.find_element_by_xpath("//span[@class='sc-bdVaJa eSMcEc']").get_attribute('textContent')
                description=d.find_element_by_xpath("//span[@data-testid='nestedItemHeader_subtitle']").get_attribute('textContent')
                price= d.find_element_by_xpath("//button[@data-anchor-id='AddToCartButton']").get_attribute('textContent')
                image=d.find_element_by_xpath("//img[@loading='lazy']").get_attribute("src")
                foods=d.find_elements_by_xpath("//div[@class='sc-bwzfXH eTjsAl']")
                foodss=[]
                for food in foods:
                    sections=[]
                    fds=food.find_elements_by_tag_name('span')
                    for fd in fds:
                        text=fd.text
                        sections.append(text)
                    foodss.append(sections)
                
                
                for xx in foodss:
                    for xxx in xx:
                      if xxx.startswith('+$'):
                        ind=xx.index(xxx)
                        new=[xx[ind-1], xxx]
                        xx[ind-1]=new
                        xx.remove(xxx)

                for xx in foodss:
                    for xxx in xx:
                        if type(xxx)== list:
                            pass
                        else:
                            ind=xx.index(xxx)
                            xx[ind]=[xxx, ""]
                
                WebDriverWait(d, 20).until(EC.presence_of_element_located((By.XPATH,"//button[@type='button']")))
                d.find_element_by_xpath("/html/body/div[1]/main/div/div[4]/div/div[2]/div/div[2]/div[1]/button").click()
                print('\n')
                
                items={}
                items['name']=meal
                items['image_url']=image
                items['description']= description
                items['display_string']= " ",
                items['item_type']="MenuPageItem"
                items['amount']=price[14:]
                
                options=[]
                for fod in foodss:
                    if fod==[]:
                        pass
                    else:
                        sub_options={}
                        sub_options['categogy_name']=fod[0][0]
                        sub_options['category_type']= fod[1][0],
                        sub_options['select_option']= fod[2][0],
                        sub_options['options_list']=fod[3:]
                        options.append(sub_options)
                items['Options']=options
                item.append(items)
             except:
                continue
    category['Name']= title
    category['items']= item
    print(category)
    Categories.append(category)
Data['restaurant_name']='Panara'
Data['Categories']=Categories

import json as js
with open('panara1.json', 'w') as fob:
    js.dump(Data, fob)

        


            

        

    
    




            
                

                

                



