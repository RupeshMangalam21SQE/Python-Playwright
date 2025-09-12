import pytest
from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage
from pages.home_page import HomePage
from playwright.async_api import expect
from config import URLS


@given("I am on the login page")
@pytest.mark.asyncio
async def open_login_page(page):
    login_page = LoginPage(page)
    await login_page.navigate(URLS["login"])
    return login_page


@when(parsers.cfparse('I enter username "{username}" and password "{password}"'))
@pytest.mark.asyncio
async def enter_credentials(page, username, password):
    login_page = LoginPage(page)
    await login_page.login(username, password)


@when("I submit the login form")
@pytest.mark.asyncio
async def submit_login(page):
    login_page = LoginPage(page)
    await login_page.submit_button.click()


@then(parsers.cfparse('I should see the welcome message "{expected_message}"'))
@pytest.mark.asyncio
async def verify_welcome_message(page, expected_message):
    home_page = HomePage(page)
    await home_page.verify_welcome_message(expected_message)


@then(parsers.cfparse('I should see the message "{expected_message}"'))
@pytest.mark.asyncio
async def verify_message(page, expected_message):
    flash_message = page.locator("#flash")
    await expect(flash_message).to_contain_text(expected_message)
