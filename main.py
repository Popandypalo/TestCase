from time import sleep
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    def __init__(self) -> None:
        self.option = webdriver.ChromeOptions()
        self.option.add_argument("--ignore-certificate-errors")
        self.option.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

        self.driver = uc.Chrome(options=self.option)
        self.driver.get('https://accounts.google.com/ServiceLogin')
        self.time = 100

    def googleAuth(self, email, password):
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(f'{email}\n')
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(f'{password}\n')

        sleep(self.time)

if __name__ == '__main__':

    email = 'popandypalowork@gmail.com'
    password = 'Chikas123'
    browser = Browser()
    browser.googleAuth(email, password)
