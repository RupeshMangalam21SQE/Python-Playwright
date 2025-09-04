from playwright.sync_api import sync_playwright

def _run_test(page):
    page.goto("https://example.com")
    print("Firefox launched in headless mode")

def test_browser_config(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=True)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_browser_config()
