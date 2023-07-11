from selenium.webdriver.common.by import By
from selenium import webdriver
from captchaai import CaptchaAI
from time import sleep

api_key = 'your_api_key'
solver = CaptchaAI(api_key)
url = 'https://site/with/normalcaptcha'
driver = webdriver.Chrome()
driver.get(url)
s = driver.find_element(By.XPATH, '//img[contains(@alt,"captcha")]')
path_to_image = s.get_attribute('src')
result = solver.normal(path_to_image, module='common-1')
WE = driver.find_element(By.XPATH, '//input[@id="simple-captcha-field"]')
print('Result=', result)
if result:
    try:
        WE.send_keys(result['code'])
        sleep(90)
    except Exception as e:
        js = f"arguments[0].setAttribute('text'," + result['code'] + ")"
        driver.execute_script(js, WE)
        sleep(90)
