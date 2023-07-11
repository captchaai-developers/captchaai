from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
import sys
import os
from captchaai import CaptchaAI

api_key = 'your_api_key'
solver = CaptchaAI(api_key)
url = 'https://site/with/recaptcha/v3'
driver = webdriver.Chrome()
driver.get(url)


s = driver.find_element(By.XPATH, '//script[contains(text(),"grecaptcha.execute")]')
info=s.get_attribute('innerHTML').split('grecaptcha.execute(')[1].split(',')
site_key = info[0]
if "'" in site_key:
    site_key=site_key.replace("'","")
site_key=site_key.replace('\n','')
site_key=site_key.replace(' ','')
action=info[1].split("'")[1]

result = solver.recaptcha(
        sitekey=site_key,
        url=url,
        version='v3',
        action=action,
        score=0.9
    )
print('Result=', result)
if result:
    js = f"window.verifyRecaptcha('"+result['code']+"');"
    print(js)
    driver.execute_script(js)
sleep(90)
