from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    # Assert URL
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

    # Assert heading exactly
    expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()


def test_successful_login(page=None):
    if page:  # Running with pytest fixture
        _run_test(page)
    else:  # Running standalone
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_successful_login()
