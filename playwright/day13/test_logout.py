from playwright.sync_api import sync_playwright, expect

def _perform_login(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

def _perform_logout(page):
    page.get_by_role("link", name="Logout").click()

def test_logout(page=None):
    if page:
        _perform_login(page)

        expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
        expect(page.locator("h2")).to_have_text("Secure Area")

        _perform_logout(page)

        expect(page).to_have_url("https://the-internet.herokuapp.com/login")
        expect(page.locator("#flash")).to_contain_text("You logged out of the secure area!")

    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            login_page = chromium_browser.new_page()

            _perform_login(login_page)
            expect(login_page).to_have_url("https://the-internet.herokuapp.com/secure")
            expect(login_page.locator("h2")).to_have_text("Secure Area")

            _perform_logout(login_page)
            expect(login_page).to_have_url("https://the-internet.herokuapp.com/login")
            expect(login_page.locator("#flash")).to_contain_text("You logged out of the secure area!")

            chromium_browser.close()

if __name__ == "__main__":
    test_logout()
