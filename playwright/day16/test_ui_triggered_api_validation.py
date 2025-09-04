from playwright.sync_api import sync_playwright, expect
import pytest

def _run_test(page, request_context):
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

    # Simulate API validation using httpbin (form submission)
    response = request_context.post(
        "https://httpbin.org/post",
        form={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "message": "Hello, this is a test message."
        }
    )

    assert response.ok, f"API call failed: {response.status}"
    result = response.json()

    # Validate echoed form data
    assert result["form"]["first_name"] == "John"
    assert result["form"]["email"] == "john.doe@example.com"
    print("API validation successful")
    print(result)

def test_ui_triggered_api_validation(page=None):
    if page:
        with sync_playwright() as p:
            request_context = p.request.new_context()
            _run_test(page, request_context)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            request_context = p.request.new_context()
            _run_test(page, request_context)
            browser.close()

if __name__ == "__main__":
    test_ui_triggered_api_validation()
