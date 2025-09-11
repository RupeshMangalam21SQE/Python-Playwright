from playwright.sync_api import sync_playwright

def _install_check(page):
    page.goto("https://example.com")

def test_install_check(page=None):
    if page:
        _install_check(page)
    else:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()
            _install_check(page)
            browser.close()

if __name__ == "__main__":
    test_install_check()
