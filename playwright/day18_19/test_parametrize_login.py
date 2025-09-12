import pytest
from playwright.sync_api import sync_playwright, expect

def _run_test(page, username, password, expected_text):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", username)
    page.fill("#password", password)
    page.click("button[type='submit']")

    # Verify flash message
    expect(page.locator("#flash")).to_contain_text(expected_text)

@pytest.mark.parametrize("username,password,expected_text", [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("tomsmith", "wrong", "Your password is invalid!"),
    ("wronguser", "SuperSecretPassword!", "Your username is invalid!"),
])
def test_login(page, username, password, expected_text):
    _run_test(page, username, password, expected_text)


if __name__ == "__main__":
    test_data = [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
        ("tomsmith", "wrong", "Your password is invalid!"),
        ("wronguser", "SuperSecretPassword!", "Your username is invalid!"),
    ]

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()

        for username, password, expected in test_data:
            page = context.new_page()
            print(f"Testing with: {username}/{password}")
            _run_test(page, username, password, expected)
            page.close()

        browser.close()
