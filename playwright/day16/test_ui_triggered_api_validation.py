from playwright.sync_api import sync_playwright, expect
import pytest

def _run_test(page):
    page.goto("https://www.webdriveruniversity.com/Contact-Us/contactus.html")

    # Fill out the contact form
    page.fill("input[name='first_name']", "John")
    page.fill("input[name='last_name']", "Doe")
    page.fill("input[name='email']", "john.doe@example.com")
    page.fill("textarea[name='message']", "Hello, this is a test message.")

    # Submit form
    page.click("input[value='SUBMIT']")

    # Verify UI response
    expect(page.locator("body")).to_contain_text("Thank You for your Message!")

    # Simulate API validation (since this form has no real API)
    response = page.request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "message": "Hello, this is a test message."
        }
    )
    assert response.ok
    result = response.json()
    assert result["first_name"] == "John"
    assert result["email"] == "john.doe@example.com"

def test_ui_triggered_api_validation(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_ui_triggered_api_validation()
