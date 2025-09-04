from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    # Assert login success
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.locator("h2")).to_have_text("Secure Area")

    # Click logout
    page.get_by_role("link", name="Logout").click()

    # Assert redirected back to login page
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")
    expect(page.locator("#flash")).to_contain_text("You logged out of the secure area!")

def test_logout(page=None):
    if page:  # Running with pytest fixture
        _run_test(page)
    else:  # Standalone run
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_logout()
