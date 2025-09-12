from playwright.async_api import expect
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = self.page.locator("[data-test='checkout']")
        self.cart_item = lambda name: self.page.locator(f".inventory_item_name:has-text('{name}')")

    async def verify_item_in_cart(self, product_name: str):
        await expect(self.cart_item(product_name)).to_be_visible()

    async def proceed_to_checkout(self):
        await self.checkout_button.click()
        return CheckoutPage(self.page)
