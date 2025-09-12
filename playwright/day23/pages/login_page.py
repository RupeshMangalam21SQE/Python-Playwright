from playwright.async_api import expect
from pages.base_page import BasePage
from pages.home_page import HomePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = self.page.locator("#username")
        self.password_input = self.page.locator("#password")
        self.submit_button = self.page.locator("button[type='submit']")

    async def navigate(self, url: str):
        await self.page.goto(url)

    async def login(self, username: str, password: str):
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.submit_button.click()

        # After login, return a HomePage object
        return HomePage(self.page)
