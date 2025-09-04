from playwright.sync_api import sync_playwright, expect
import pytest, json

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Intercept API call and return instantly with mock data
    def handle_route(route):
        mock_data = {"message": "Mocked response!"}
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(mock_data)
        )

    page.route("**/dynamic_loading/2", handle_route)

    page.click("button")  # Start loading
    expect(page.locator("#finish")).to_be_visible(timeout=5000)

def test_mocking_slow_api(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_mocking_slow_api()
