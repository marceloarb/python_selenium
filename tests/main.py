import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")
    # def test_python_dot_org(self):
    # self.driver.get("http://www.python.org")
    # assert "Python" in self.driver.title
    # logger.info(f"the self.driver title is: {self.driver.title}")
    # elem = self.driver.find_element(By.NAME, value="q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in self.driver.page_source
    # self.driver.close()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()