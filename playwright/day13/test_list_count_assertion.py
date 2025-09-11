from playwright.sync_api import sync_playwright, expect

def _get_checkboxes(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    return page.locator("input[type=checkbox]")

def test_list_count_assertion(page=None):
    if page:
        checkboxes = _get_checkboxes(page)
        expect(checkboxes).to_have_count(2)
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            checkbox_page = chromium_browser.new_page()

            checkboxes = _get_checkboxes(checkbox_page)
            expect(checkboxes).to_have_count(2)

            chromium_browser.close()

if __name__ == "__main__":
    test_list_count_assertion()
