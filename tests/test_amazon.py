import pytest
import logging
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.select import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
logger = logging.getLogger(__name__)
load_dotenv()

@pytest.fixture
def visible_chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

class Amazon():
    SEARCH_BAR = (By.NAME, "field-keywords")
    def __init__(self,driver):
        self.url = os.getenv("AMAZON_URL")
        self.driver = driver

    def amazon_search(self,search_term):
        search_element = self.driver.find_element(*self.SEARCH_BAR)
        search_element.clear()
        search_element.send_keys(search_term)
        search_element.send_keys(Keys.RETURN)

    def get_prices(self):
        prices_holder = self.driver.find_elements(By.CSS_SELECTOR, "span.a-offscreen")
        print(len(prices_holder))
        for price in prices_holder:
            print(price.text)
def test_amazon_ring(visible_chrome_driver):
    amazon = Amazon(visible_chrome_driver)
    amazon.driver.maximize_window()
    amazon.driver.get(amazon.url)
    assert "Amazon" in amazon.driver.title
    amazon.amazon_search("ring camera")
    try:
        WebDriverWait(amazon.driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-color-state.a-text-bold"))
        )
        amazon.get_prices()
    except Exception as e:
        logger.error(e)