import os
import pytest
import allure
from datetime import datetime
from playwright.async_api import async_playwright


os.makedirs("reports/allure-results", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run tests in headed mode (browser UI visible)"
    )


@pytest.fixture
def headed(request):
    return request.config.getoption("--headed")


@pytest.fixture(scope="function")
async def browser(headed):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not headed, slow_mo=300 if headed else 0)
        yield browser
        await browser.close()


@pytest.fixture(scope="function")
async def page(browser):
    page = await browser.new_page()
    yield page
    if hasattr(pytest, "test_outcome") and pytest.test_outcome.get("failed"):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            worker_id = os.environ.get('PYTEST_XDIST_WORKER', '')
            screenshot_path = os.path.join("screenshots", f"failure_{pytest.test_name}_{worker_id}_{timestamp}.png")
            await page.screenshot(path=screenshot_path, full_page=True)
            allure.attach.file(screenshot_path, name="failure_screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
    await page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        setattr(pytest, "test_outcome", {"failed": rep.failed})
        setattr(pytest, "test_name", item.name)
