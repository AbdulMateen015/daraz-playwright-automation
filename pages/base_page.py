from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)
        self.handle_popups()

    def handle_popups(self):
        """
        Check for common Daraz overlays (App download, Location, etc.) and close them.
        """
        try:
            close_btn = self.page.locator(".close-btn, .button-close, [aria-label='Close']").first
            if close_btn.is_visible(timeout=2000):
                close_btn.click()
        except Exception:
            pass

    def get_title(self) -> str:
        return self.page.title()
