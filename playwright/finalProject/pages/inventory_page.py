from playwright.async_api import expect
from pages.base_page import BasePage
from pages.cart_page import CartPage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_item = lambda name: self.page.locator(f".inventory_item_name:has-text('{name}')")
        self.add_to_cart_button = lambda name: self.page.locator(f"[data-test='add-to-cart-{name.lower().replace(' ', '-')}']")
        self.cart_icon = self.page.locator(".shopping_cart_link")

    async def search_for_product(self, product_name: str):
        # Sauce Demo doesn't have a search bar; simulate by checking visibility
        await expect(self.product_item(product_name)).to_be_visible(timeout=5000)

    async def add_product_to_cart(self, product_name: str):
        await self.add_to_cart_button(product_name).click()

    async def go_to_cart(self):
        await self.cart_icon.click()
        return CartPage(self.page)
