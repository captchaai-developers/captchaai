from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_CAPCHAAI=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_CAPCHAAI=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')
your_site_with_captcha = 'https://squareblogs.net/signup'

from captcha_ai import CaptchaAI

solver = CaptchaAI(api_key)

url = your_site_with_captcha
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
