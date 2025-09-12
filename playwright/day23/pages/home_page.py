from playwright.async_api import expect
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.welcome_message = self.page.locator("#flash")

    async def verify_welcome_message(self, expected_text: str):
        await expect(self.welcome_message).to_contain_text(expected_text)
