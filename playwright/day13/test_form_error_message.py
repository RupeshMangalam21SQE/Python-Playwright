from playwright.sync_api import sync_playwright, expect

def _attempt_login(page, username="tomsmith", password="wrongpass"):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    return page

def test_form_error_message(page=None):
    if page:
        login_page = _attempt_login(page, password="wrongpass")
        expect(login_page).to_have_url("https://the-internet.herokuapp.com/login")
        expect(login_page.locator("#flash")).to_contain_text("Your password is invalid!")
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            login_page = chromium_browser.new_page()

            login_page = _attempt_login(login_page, password="wrongpass")

            expect(login_page).to_have_url("https://the-internet.herokuapp.com/login")
            expect(login_page.locator("#flash")).to_contain_text("Your password is invalid!")

            chromium_browser.close()

if __name__ == "__main__":
    test_form_error_message()
