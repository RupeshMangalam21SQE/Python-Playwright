from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option("2")
    expect(dropdown).to_have_value("2")

    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox = page.locator("input[type='checkbox']").first
    checkbox.check()
    expect(checkbox).to_be_checked()

def test_dropdown_checkbox(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_dropdown_checkbox()
