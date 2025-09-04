from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = page.locator("input[type=checkbox]")
    expect(checkboxes).to_have_count(2)

def test_list_count_assertion(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()
