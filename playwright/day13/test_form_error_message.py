from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("wrongpass")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://the-internet.herokuapp.com/login")
    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")

def test_form_error_message(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()
