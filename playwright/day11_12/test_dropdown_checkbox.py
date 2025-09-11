from playwright.sync_api import sync_playwright, expect

def _select_dropdown_option(page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option("2")
    return dropdown

def _check_first_checkbox(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox = page.locator("input[type='checkbox']").first
    checkbox.check()
    return checkbox

def test_dropdown_checkbox(page=None):
    if page:
        dropdown = _select_dropdown_option(page)
        expect(dropdown).to_have_value("2")

        checkbox = _check_first_checkbox(page)
        expect(checkbox).to_be_checked()
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            test_page = chromium_browser.new_page()

            dropdown = _select_dropdown_option(test_page)
            expect(dropdown).to_have_value("2")

            checkbox = _check_first_checkbox(test_page)
            expect(checkbox).to_be_checked()

            chromium_browser.close()

if __name__ == "__main__":
    test_dropdown_checkbox()
