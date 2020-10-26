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

class Google_United():
    SEARCH_BAR = (By.NAME, "q")
    def __init__(self,driver):
        self.url = os.getenv("GOOGLE_URL")
        self.driver = driver
    def google_search(self,search_term):
        search_element = self.driver.find_element(*self.SEARCH_BAR)
        search_element.clear()
        search_element.send_keys(search_term)
        search_element.send_keys(Keys.RETURN)
        
def test_united_input(visible_chrome_driver):
    google = Google_United(visible_chrome_driver)
    google.driver.get(google.url)
    assert "Google" in google.driver.title
    google.google_search("united airlines")
    try:
            main = WebDriverWait(google.driver,10).until(
                EC.presence_of_element_located((By.ID, "search"))
            )
            class_name = main.find_element(By.CLASS_NAME, value="yuRUbf")
            united = class_name.find_element(By.TAG_NAME, value="a")
            united.click()
            input_from = google.driver.find_element(By.ID, value="bookFlightOriginInput")
            input_from.send_keys(Keys.CONTROL + "a")
            input_from.send_keys(Keys.DELETE)
            input_from.send_keys("Dallas, TX, US (DFW - All Airports)")
            input_from.send_keys(Keys.DOWN)
            input_from.send_keys(Keys.RETURN)
            input_to = google.driver.find_element(By.ID, value="bookFlightDestinationInput")
            input_to.send_keys("São Paulo, SP, BR (GRU)" )
            input_to.send_keys(Keys.DOWN)
            input_to.send_keys(Keys.RETURN)
            input_depart_date = google.driver.find_element(By.NAME, value="DepartDate")
            input_depart_date.send_keys(Keys.CONTROL + "a")
            input_depart_date.send_keys(Keys.DELETE)
            input_depart_date.send_keys("Oct 30")
            return_date = google.driver.find_element(By.NAME, value="ReturnDate")
            return_date.send_keys(Keys.CONTROL + "a")
            return_date.send_keys(Keys.DELETE)
            return_date.send_keys("NOV 13")
            return_date.send_keys(Keys.ESCAPE)
            button = google.driver.find_element(By.CSS_SELECTOR, value="#bookFlightForm > div.app-components-BookFlightForm-bookFlightForm__basicEconomyToggle--1VE5O > div > div:nth-child(1) > div > div > button")
            button.click()
            google.driver.save_screenshot("Hello.png")
    except Exception as e:
        logger.error(e)


   
    