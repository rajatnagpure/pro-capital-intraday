from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from constants import *
import bs4
import os


class website:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        self.wait = WebDriverWait(self.browser, 10)

    def login(self):
        self.browser.get(LoginURL)
        try:
            username_box = self.wait.until(
                lambda driver: self.browser.find_element_by_xpath(UsernameXpath))
            password_box = self.wait.until(
                lambda driver: self.browser.find_element_by_xpath(PasswordXpath))
            login_button = self.wait.until(
                lambda driver: self.browser.find_element_by_xpath(LoginButtonXpath))

            username_box.clear()
            password_box.clear()
            username_box.send_keys(Username)
            password_box.send_keys(Password)
            login_button.click()
            print('Login Successful')

        except Exception as e:
            print('failed to login {}'.format(str(e)))
        self.browser.get(IntradayURL)

    def get_call(self):
        self.browser.refresh()
        self.wait.until(lambda driver: self.browser.find_element_by_xpath(CallTableRow))
        soup = bs4.BeautifulSoup(self.browser.page_source, 'lxml')
        table = soup.table
        table_rows = table.find_all('tr')
        tr = table_rows[2]
        td = tr.find_all('td')
        row = [i.text for i in td]
        return row

    def stop_browser(self):
        self.browser.quit()