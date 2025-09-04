from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/hovers")
    figure = page.locator(".figure").first
    figure.hover()
    caption = figure.locator(".figcaption h5")
    expect(caption).to_be_visible()

def test_hover_and_click(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_hover_and_click()
