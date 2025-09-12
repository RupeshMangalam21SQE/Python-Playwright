import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.home_page import HomePage
from playwright.async_api import expect
from config import URLS


# Link to the feature file
scenarios("../features/login.feature")


# ---- Fixtures ----
@pytest.fixture
async def login_page(page):
    """Provide the LoginPage object."""
    return LoginPage(page)


# ---- Step Definitions ----

# Step: Given I am on the login page
@given("I am on the login page")
@pytest.mark.asyncio
async def open_login_page(login_page):
    await login_page.navigate(URLS["login"])
    return login_page


# Step: When I enter username "<username>" and password "<password>"
@when('I enter username "<username>" and password "<password>"')  # VSCode IntelliSense
@when(parsers.cfparse('I enter username "{username}" and password "{password}"'))
@pytest.mark.asyncio
async def enter_credentials(login_page, username, password):
    await login_page.login(username, password)


# Step: And I submit the login form
@when("I submit the login form")
@pytest.mark.asyncio
async def submit_login(login_page):
    await login_page.submit_button.click()


# Step: Then I should see the welcome message "<expected_message>"
@then('I should see the welcome message "<expected_message>"')  # VSCode IntelliSense
@then(parsers.cfparse('I should see the welcome message "{expected_message}"'))
@pytest.mark.asyncio
async def verify_welcome_message(login_page, expected_message):
    home_page = HomePage(login_page.page)
    await home_page.verify_welcome_message(expected_message)


# Step: Then I should see the message "<expected_message>"
@then('I should see the message "<expected_message>"')
@then(parsers.cfparse('I should see the message "{expected_message}"'))
@pytest.mark.asyncio
async def verify_message(login_page, expected_message):
    flash_message = login_page.page.locator("#flash")
    await expect(flash_message).to_contain_text(expected_message)
