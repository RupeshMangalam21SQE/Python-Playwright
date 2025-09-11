from playwright.sync_api import sync_playwright, expect

def _navigate_to_homepage(page):
    page.goto("https://playwright.dev/")

def test_first_script(page=None):
    if page:
        _navigate_to_homepage(page)
        expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            homepage = chromium_browser.new_page()
            _navigate_to_homepage(homepage)
            expect(homepage).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
            chromium_browser.close()

if __name__ == "__main__":
    test_first_script()
