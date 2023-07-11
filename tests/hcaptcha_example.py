from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
import sys
import os
from captchaai import CaptchaAI

api_key = 'your_api_key'
solver = CaptchaAI(api_key)



url = 'https://site/with/hcaptcha'
driver = webdriver.Chrome()
driver.get(url)
sleep(5)
s = driver.find_element(By.XPATH, '//iframe') #here use the xpath of the element that contains the site key,you can find it by opening the developer tab in the website
site_key= s.get_attribute('src').split('sitekey=')[1].split('&')[0] #the site scraped here didn't contain the sitekey as an attribute but it was included in a url value of the src attribute that's why I splitted it this way
print(site_key)

result = solver.hcaptcha(sitekey=site_key,url=url)

WE = driver.find_element(By.XPATH, '//textarea[@name="h-captcha-response"]')
print('Result=', result)
if result:
    js = f"arguments[0].setAttribute('style','')"
    driver.execute_script(js, WE)  # to make the textarea visible to place the code in it.

    try:
        WE.send_keys(result['code'])
    except:
        js = f"arguments[0].setAttribute('text'," + result['code'] + ")"
        driver.execute_script(js, WE)

print('Result=', result)
