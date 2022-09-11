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

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
