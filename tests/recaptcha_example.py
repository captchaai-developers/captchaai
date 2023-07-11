from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
import sys
import os
from captchaai import CaptchaAI
api_key = 'your_api_key'
solver = CaptchaAI(api_key)
url = 'https://site/with/normalcaptcha'
driver = webdriver.Chrome()
driver.get(url)
s = driver.find_element(By.XPATH, '//div[@class="g-recaptcha"]')
site_key = s.get_attribute('data-sitekey')

result = solver.recaptcha(
    sitekey=site_key,
    url=url)
WE = driver.find_element(By.XPATH, '//textarea[contains(@id,"g-recaptcha-response")]')
print('Result=', result)
if result:
    js = f"arguments[0].setAttribute('style','')"
    driver.execute_script(js, WE)  # to make the textarea visible to place the code in it.

    try:
        WE.send_keys(result['code'])
    except:
        js = f"arguments[0].setAttribute('text'," + result['code'] + ")"
        driver.execute_script(js, WE)
