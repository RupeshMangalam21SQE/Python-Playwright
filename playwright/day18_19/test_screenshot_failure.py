from playwright.sync_api import sync_playwright, expect
import time
import os

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "wrong")
    page.fill("#password", "wrong")
    page.click("button[type='submit']")

    try:
        # Expect the success message (will fail here)
        expect(page.locator("#flash")).to_contain_text("You logged into a secure area!", timeout=2000)
    except Exception as e:
        # Create unique screenshot name with timestamp
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path = f"failure_{timestamp}.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Test failed. Screenshot saved: {os.path.abspath(screenshot_path)}")
        raise e

def test_screenshot_failure():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            _run_test(page)
        finally:
            browser.close()

if __name__ == "__main__":
    test_screenshot_failure()
