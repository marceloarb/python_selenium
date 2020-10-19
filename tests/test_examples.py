import pytest
import logging
from selenium import webdriver
from selenium.webdriver.support.select import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
logger = logging.getLogger(__name__)


# driver = webdriver.Remote(
#         command_executor="http://localhost:4444",
#         desired_capabilities=DesiredCapabilities.CHROME,
#     )

visible_driver = webdriver.Chrome()

def test_python_dot_org():
    visible_driver.get("http://www.python.org")
    assert "Python" in visible_driver.title
    logger.info(f"the visible_driver title is: {visible_driver.title}")
    elem = visible_driver.find_element(By.NAME, value="q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in visible_driver.page_source
    visible_driver.close()


# def test_google_search_bar():
#     driver.get("https://www.google.com/")
#     assert "Google" in driver.title
#     logger.info(f"the driver title is: {driver.title}")
#     element = driver.find_element(By.NAME, value="q")
#     element.clear()
#     element.send_keys("dolar hoje real")
#     element.send_keys(Keys.RETURN)
#     assert "Brazilian Real" in driver.page_source
#     logger.info(f"the driver title after search is: {driver.title}")
#     driver.close()
    
    
def test_google_united():
    visible_driver.get("https://www.google.com/")
    assert "Google" in visible_driver.title
    element =  visible_driver.find_element(By.NAME, value="q")
    element.clear()
    element.send_keys("united airlines" + Keys.ENTER)
    try:
        main = WebDriverWait(visible_driver,10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        class_name = main.find_element(By.CLASS_NAME, value="yuRUbf")
        united = class_name.find_element(By.TAG_NAME, value="a")
        united.click()
        test_united_input()
    finally:
        visible_driver.close()

def test_united_input():
    input_from = visible_driver.find_element(By.ID, value="bookFlightOriginInput")
    input_from.send_keys(Keys.CONTROL + "a")
    input_from.send_keys(Keys.DELETE)
    input_from.send_keys("Dallas, TX, US (DFW - All Airports)")
    input_from.send_keys(Keys.DOWN)
    input_from.send_keys(Keys.RETURN)
    input_to = visible_driver.find_element(By.ID, value="bookFlightDestinationInput")
    input_to.send_keys("São Paulo, SP, BR (GRU)" )
    input_to.send_keys(Keys.DOWN)
    input_to.send_keys(Keys.RETURN)
    input_depart_date = visible_driver.find_element(By.NAME, value="DepartDate")
    input_depart_date.send_keys(Keys.CONTROL + "a")
    input_depart_date.send_keys(Keys.DELETE)
    input_depart_date.send_keys("Oct 30")
    return_date = visible_driver.find_element(By.NAME, value="ReturnDate")
    return_date.send_keys(Keys.CONTROL + "a")
    return_date.send_keys(Keys.DELETE)
    return_date.send_keys("NOV 13")
    return_date.send_keys(Keys.ESCAPE)
    button = visible_driver.find_element(By.CSS_SELECTOR, value="#bookFlightForm > div.app-components-BookFlightForm-bookFlightForm__basicEconomyToggle--1VE5O > div > div:nth-child(1) > div > div > button")
    button.click()
    visible_driver.save_screenshot("Hello.png")




# def test_united_airline_homepage():
#     driver.get("https://www.united.com/en/us")
#     assert "United" in driver.title
#     logger.info(f"the driver title is: {driver.title}")
#     element_from = driver.find_element(By.ID, value="bookFlightOriginInput")
#     element_from.clear()
#     element_from.send_keys("Dallas DFW ")
#     driver.implicitly_wait(1)
#     element_to = driver.find_element(By.ID, value="bookFlightDestinationInput")
#     element_to.clear()
#     element_to.send_keys("São Paulo SAO")
#     driver.implicitly_wait(10)
#     element_depart_date = driver.find_element(By.ID, value=("DepartDate"))
#     element_depart_date.send_keys("Oct 30")
#     driver.implicitly_wait(1)
#     element_return_date = driver.find_element(By.ID, value=("ReturnDate"))
#     element_return_date.send_keys("Nov 21")
#     driver.implicitly_wait(10)
#     submit =  driver.find_element(By.XPATH, value="//*[@id='bookFlightForm']/div[4]/div/div[1]/div/div/button")
#     action = ActionChains(driver) 
#     action.click(on_element = submit)
#     assert "No results found." not in driver.page_source
#     driver.close()

# def test_united_airline_homepage1():
#     driver.get("https://www.united.com/en/us")
#     assert "United" in driver.title
#     logger.info(f"the driver title is: {driver.title}")
#     element_from = driver.find_element(By.ID, value="bookFlightOriginInput")
#     element_from.clear()
#     element_from.send_keys("Dallas DFW ")
#     element_from.send_keys(Keys.TAB)
#     element_from.send_keys("São Paulo SAO")
#     element_from.send_keys(Keys.TAB)
#     element_from.send_keys(Keys.TAB)
#     element_from.send_keys("Oct 30")
#     element_from.send_keys("Nov 21")
#     driver.implicitly_wait(10)
#     submit =  driver.find_element(By.XPATH, value="//*[@id='bookFlightForm']/div[4]/div/div[1]/div/div/button")
#     action = ActionChains(driver) 
#     action.click(on_element = submit)
#     assert "No results found." not in driver.page_source
#     driver.close()



   
    