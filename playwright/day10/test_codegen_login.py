from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill('input[name="username"]', "tomsmith")
    page.fill('input[name="password"]', "SuperSecretPassword!")
    page.click('button[type="submit"]')
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.locator("h2")).to_have_text("Secure Area")

def test_codegen_login(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_codegen_login()
