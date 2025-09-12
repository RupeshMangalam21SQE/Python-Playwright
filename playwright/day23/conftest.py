import os
import pytest
import allure
from datetime import datetime
from playwright.async_api import async_playwright
import pytest
from pytest_bdd import scenario

# Ensure screenshots folder exists
os.makedirs("screenshots", exist_ok=True)

# Browser fixture for test isolation (async)
@pytest.fixture(scope="function")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        yield browser
        await browser.close()

# Page fixture with auto-screenshot on failure
@pytest.fixture(scope="function")
async def page(browser):
    page = await browser.new_page()
    yield page
    # Teardown: Check if test failed and capture screenshot if so
    if hasattr(pytest, "test_outcome") and pytest.test_outcome.get("failed"):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            worker_id = os.environ.get('PYTEST_XDIST_WORKER', '')  # For uniqueness in parallel runs
            screenshot_path = os.path.join("screenshots", f"failure_{pytest.test_name}_{worker_id}_{timestamp}.png")
            await page.screenshot(path=screenshot_path, full_page=True)
            allure.attach.file(screenshot_path, name="failure_screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
    await page.close()

# Hook to track test outcome and name for fixtures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # Store outcome and test name globally for fixture access
    if rep.when == "call":
        setattr(pytest, "test_outcome", {"failed": rep.failed})
        setattr(pytest, "test_name", item.name)

def pytest_bdd_apply_tag(tag, function):
    if tag == 'asyncio':
        marker = pytest.mark.asyncio
        marker(function)
        return True
    return False