from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
    

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome()

old_service = ''

url = 'https://khamsat.com/community/requests/737565-%D9%86%D8%B5-%D9%85%D9%81%D8%B1%D8%BA-%D9%8A%D8%AD%D8%AA%D8%A7%D8%AC-%D8%A7%D9%84%D9%89-%D9%85%D8%B1%D8%A7%D8%AC%D8%B9%D8%A9'

while True :
    driver.get(url)
    time.sleep(2)
    all_services = driver.find_elements(By.CSS_SELECTOR, '.o-media__body.pt-2 h5 a')
    service = all_services[0]

    if  old_service != service.text:
        notify('طلب خدمة جديد', service.text)
        print(f"""
        {"="*50}
        الخدمة: {service.text}
        رابط الخدمة: {service.get_attribute('href')}
        """)
        old_service = service.text

    time.sleep(60)
