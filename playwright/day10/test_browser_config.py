from playwright.sync_api import sync_playwright

def _run_test(page):
    page.goto("https://example.com")

def test_browser_config(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as playwright:
            firefox_browser = playwright.firefox.launch(headless=True)
            test_page = firefox_browser.new_page()
            _run_test(test_page)
            firefox_browser.close()

if __name__ == "__main__":
    test_browser_config()
