from playwright.sync_api import sync_playwright, expect

def _perform_login(page, username="tomsmith", password="SuperSecretPassword!"):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", username)
    page.fill("#password", password)
    page.click("button[type='submit']")
    return page

def test_login_form(page=None):
    if page:
        login_page = _perform_login(page)
        expect(login_page).to_have_url("https://the-internet.herokuapp.com/secure")
        expect(login_page.locator("h2")).to_have_text("Secure Area")
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            login_page = chromium_browser.new_page()

            login_page = _perform_login(login_page)

            expect(login_page).to_have_url("https://the-internet.herokuapp.com/secure")
            expect(login_page.locator("h2")).to_have_text("Secure Area")

            chromium_browser.close()

if __name__ == "__main__":
    test_login_form()
