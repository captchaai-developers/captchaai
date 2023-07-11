from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
import sys
import os
from captchaai import CaptchaAI

api_key = '238f195955911ee1644dbe88473f02c3'
solver = CaptchaAI(api_key)



url = 'https://2captcha.com/demo/recaptcha-v2-invisible'
driver = webdriver.Chrome()
driver.get(url)
sleep(5)
s = driver.find_element(By.XPATH, '//div[@id="g-recaptcha"]')
site_key = s.get_attribute('data-sitekey')
print(site_key)

result = solver.recaptcha(
        sitekey=site_key,
        url=url,
        invisible=1)
print('result',result)
print('Result=', result)
if result:
    WE = driver.find_element(By.XPATH, '//textarea[contains(@id,"g-recaptcha-response")]')
    js = f"arguments[0].setAttribute('style','')"
    driver.execute_script(js, WE)
    WE1 = driver.find_element(By.XPATH, '//div[@class="grecaptcha-badge"]')
    driver.execute_script(js, WE1)  # to make the textarea visible to place the code in it.

    try:
        WE.send_keys(result['code'])
        sleep(90)
    except:
        js = f"arguments[0].setAttribute('text','" + result['code'] + "')"
        driver.execute_script(js, WE)
        sleep(90)

print('\n\nResult=', result)

