import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self) -> None:
        chrome_driver_path = r"C:\Development\chromedriver"
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://www.python.org")

    def test_title(self):
       mainPage = page.MainPage()
       assert mainPage.is_title_matches()

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
