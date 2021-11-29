from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Tests(TestCase):
    def test_EK(self):
        search_request = 'playstation'
        url = "https://rozetka.com.ua/ua/"

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)

        browser.get(url)

        browser.find_element(by=By.CLASS_NAME, value='search-form__input').send_keys(search_request)
        browser.find_element(by=By.CLASS_NAME, value='search-form__input').send_keys(Keys.ENTER)

        actualResult = browser.find_element(by=By.CLASS_NAME, value='goods-tile__title').text.lower()

        expectedResult = search_request

        assert expectedResult in actualResult

        browser.close()