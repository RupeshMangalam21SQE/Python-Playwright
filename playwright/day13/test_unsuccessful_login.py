from playwright.sync_api import sync_playwright, expect

def _perform_login(page, username, password):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Login").click()

def test_unsuccessful_login(page=None):
    if page:
        _perform_login(page, "wronguser", "wrongpass")

        expect(page).to_have_url("https://the-internet.herokuapp.com/login")
        expect(page.locator("#flash")).to_contain_text("Your username is invalid!")

    else: 
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            login_page = chromium_browser.new_page()

            _perform_login(login_page, "wronguser", "wrongpass")

            expect(login_page).to_have_url("https://the-internet.herokuapp.com/login")
            expect(login_page.locator("#flash")).to_contain_text("Your username is invalid!")

            chromium_browser.close()

if __name__ == "__main__":
    test_unsuccessful_login()
