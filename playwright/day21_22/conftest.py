import os
import pytest
import allure
from datetime import datetime
from playwright.async_api import async_playwright
from config import BASE_URL

# Ensure screenshots folder exists
os.makedirs("screenshots", exist_ok=True)

# Browser fixture
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

    # Start at base URL (so tests can just navigate to paths if they want)
    await page.goto(BASE_URL)

    yield page

    # Teardown: Capture screenshot if test failed
    if hasattr(pytest, "test_outcome") and pytest.test_outcome.get("failed"):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            worker_id = os.environ.get('PYTEST_XDIST_WORKER', '')
            screenshot_path = os.path.join(
                "screenshots",
                f"failure_{pytest.test_name}_{worker_id}_{timestamp}.png"
            )
            await page.screenshot(path=screenshot_path, full_page=True)
            allure.attach.file(
                screenshot_path,
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
    await page.close()

# Hook to track test outcome and name
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        setattr(pytest, "test_outcome", {"failed": rep.failed})
        setattr(pytest, "test_name", item.name)
