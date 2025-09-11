from playwright.sync_api import sync_playwright, expect

def _perform_login(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

def test_successful_login(page=None):
    if page:
        _perform_login(page)

        expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
        expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()

    else: 
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            login_page = chromium_browser.new_page()

            _perform_login(login_page)

            expect(login_page).to_have_url("https://the-internet.herokuapp.com/secure")
            expect(login_page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()

            chromium_browser.close()

if __name__ == "__main__":
    test_successful_login()
