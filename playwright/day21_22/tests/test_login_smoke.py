import pytest
from config import URLS
from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_login_pom(page):
    login_page = LoginPage(page)
    await login_page.navigate(URLS["login"])

    home_page = await login_page.login("tomsmith", "SuperSecretPassword!")
    await home_page.verify_welcome_message("You logged into a secure area!")
