from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.shipping_section = page.locator(".delivery-option-item__title")

    def get_shipping_info(self) -> str:
        self.shipping_section.first.wait_for(state="visible", timeout=10000)
        
        delivery_content = self.page.locator(".pdp-block.delivery").text_content()
        
        if "Free Shipping" in delivery_content or "Free Delivery" in delivery_content:
            return "Free Shipping Available"
        return "Standard Shipping"
