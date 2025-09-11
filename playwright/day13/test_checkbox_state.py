from playwright.sync_api import sync_playwright, expect

def _check_first_checkbox(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox = page.locator("input[type=checkbox]").first
    checkbox.check()
    return checkbox

def test_checkbox_state(page=None):
    if page:
        checkbox = _check_first_checkbox(page)
        expect(checkbox).to_be_checked()
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            checkbox_page = chromium_browser.new_page()

            checkbox = _check_first_checkbox(checkbox_page)
            expect(checkbox).to_be_checked()

            chromium_browser.close()

if __name__ == "__main__":
    test_checkbox_state()
