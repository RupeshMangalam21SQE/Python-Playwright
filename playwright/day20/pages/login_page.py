from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.home_page import HomePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "button[type='submit']"

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.submit_button)

        # After login, return a HomePage object
        return HomePage(self.page)
