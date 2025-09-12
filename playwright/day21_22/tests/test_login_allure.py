import allure
import pytest
from playwright.async_api import expect
from config import URLS

@allure.feature("Login")
@allure.story("Valid login flow")
@pytest.mark.asyncio
async def test_login_allure(page):
    with allure.step("Open login page"):
        await page.goto(URLS["login"])

    with allure.step("Fill credentials and submit"):
        await page.fill("#username", "tomsmith")
        await page.fill("#password", "SuperSecretPassword!")
        await page.click("button[type='submit']")

    with allure.step("Verify successful login message"):
        await expect(page.locator("#flash")).to_contain_text(
            "You logged into a secure area!"
        )
