from pages.base_page import BasePage
from playwright.sync_api import expect

class SearchResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.brand_list_section = page.locator("body") 
        self.price_min_input = page.get_by_placeholder("Min")
        self.price_max_input = page.get_by_placeholder("Max")
        self.price_apply_btn = page.locator(".ant-btn-primary.ant-btn-icon-only")
        self.results_grid = page.locator("div[data-qa-locator='product-item']")

    def select_first_available_brand(self):
        # Find the first available brand checkbox
        brand_checkbox = self.brand_list_section.locator(".ant-checkbox-wrapper").first
        brand_checkbox.wait_for(state="visible", timeout=10000)
        brand_checkbox.click()
        
    def filter_by_price(self, min_price: str, max_price: str):
        self.price_min_input.fill(min_price)
        self.price_max_input.fill(max_price)
        self.price_apply_btn.click()

    def get_results_count(self) -> int:
        self.results_grid.first.wait_for(state="visible", timeout=10000)
        return self.results_grid.count()

    def click_first_product(self):
        self.results_grid.first.click()
