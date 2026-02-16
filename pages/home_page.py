from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.search_input = page.get_by_placeholder("Search in Daraz")
        if not self.search_input: 
             self.search_input = page.locator("input[type='search']")
             
        self.search_button = page.locator(".search-box__button--1oH7, button.search-box__button--1oH7")

    def search_for_product(self, text: str):
        self.page.get_by_placeholder("Search in Daraz").fill(text)
        self.page.get_by_placeholder("Search in Daraz").press("Enter")
