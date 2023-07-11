from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
import sys
import os
from captchaai import CaptchaAI

api_key = '238f195955911ee1644dbe88473f02c3'
solver = CaptchaAI(api_key)



url = 'https://2captcha.com/demo/hcaptcha'
driver = webdriver.Chrome()
driver.get(url)
sleep(5)
s = driver.find_element(By.XPATH, '//iframe')
site_key= s.get_attribute('src').split('sitekey=')[1].split('&')[0]
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
