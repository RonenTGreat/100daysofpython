from locator import *
from element import BasePageElement

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultPage(BasePage):

    def is_result_found(self):
        return "No results found." not in self.driver.page_source
