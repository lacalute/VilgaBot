from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from conf import *

#get_date(0)
url = 'https://school.karelia.ru/auth/esia/send-authn-request'
def get_html(date: str):
  with open('/home/bot-schedule/dz_page.txt', 'w') as file:
    pass
  try:
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # '/usr/bin/chromedriver', chrome_options=chrome_options
    brow = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
    brow.get(url)
    time.sleep(3)
    brow.find_element(By.ID, 'login').send_keys(phone)
    brow.find_element(By.ID, 'password').send_keys(password)
    # 6 steps proccess
    aut = WebDriverWait(brow, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "plain-button_wide")))
    aut.click()
    time.sleep(1)
    aut2 = WebDriverWait(brow, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'plain-button-inline')))
    aut2.click()
    aut4 = WebDriverWait(brow, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"#homework")]')))
    aut4.click()
    aut5 = WebDriverWait(brow, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.right .top .calendar_btn > .ico, .right .top .calendar_btn.active:hover > .ico')))
    aut5.click() 
    aut6 = WebDriverWait(brow, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(@class,'ui-state-default') and //text()='{date}']")))
    aut6.click()
    time.sleep(5)
    with open('/home/bot-schedule/dz_page.txt', 'w') as file:
      file.write(brow.page_source)
    brow.quit()
  except Exception as _ex: 
    print("Error", _ex)
    brow.quit()
    return get_html(date)


#<div class="overlay" style="display: block;"></div>

#r=requests.get('<MY_URI>', auth=('<YOUR_USERNAME>', '<YOUR_PASSWORD>'))