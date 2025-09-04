from playwright.sync_api import sync_playwright

def _run_test(page):
    # Just verify browser launch works
    page.goto("https://example.com")
    print("Playwright installation check passed")

def test_install_check(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_install_check()
