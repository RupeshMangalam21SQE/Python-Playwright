from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("wronguser")
    page.get_by_label("Password").fill("wrongpass")
    page.get_by_role("button", name="Login").click()

    # Assert URL stays on login
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")

    # Assert error message is visible
    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")

def test_unsuccessful_login(page=None):
    if page:  # Running with pytest fixture
        _run_test(page)
    else:  # Standalone execution
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_unsuccessful_login()
