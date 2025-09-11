from playwright.sync_api import sync_playwright, expect

def _perform_login(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill('input[name="username"]', "tomsmith")
    page.fill('input[name="password"]', "SuperSecretPassword!")
    page.click('button[type="submit"]')

def test_codegen_login(page=None):
    if page:
        _perform_login(page)
        expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
        expect(page.locator("h2")).to_have_text("Secure Area")
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            login_page = chromium_browser.new_page()
            _perform_login(login_page)
            expect(login_page).to_have_url("https://the-internet.herokuapp.com/secure")
            expect(login_page.locator("h2")).to_have_text("Secure Area")

            chromium_browser.close()

if __name__ == "__main__":
    test_codegen_login()
