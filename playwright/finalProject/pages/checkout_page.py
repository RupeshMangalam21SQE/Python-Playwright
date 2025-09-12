from playwright.async_api import expect
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.summary_item = lambda name: self.page.locator(f".inventory_item_name:has-text('{name}')")

    async def verify_item_in_summary(self, product_name: str):
        await expect(self.summary_item(product_name)).to_be_visible()
