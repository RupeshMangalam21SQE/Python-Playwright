from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkbox1 = page.locator("input[type=checkbox]").nth(0)
    checkbox1.check()
    expect(checkbox1).to_be_checked()

def test_checkbox_state(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()
