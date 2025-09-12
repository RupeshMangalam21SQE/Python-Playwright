from playwright.async_api import expect
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = self.page.locator("[data-test='username']")
        self.password_input = self.page.locator("[data-test='password']")
        self.submit_button = self.page.locator("[data-test='login-button']")

    async def login(self, username: str, password: str):
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.submit_button.click()
        return InventoryPage(self.page)
