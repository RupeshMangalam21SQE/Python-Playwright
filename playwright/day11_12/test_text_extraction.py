from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/typos")
    text = page.locator("div.example p").nth(1).inner_text()
    print("Extracted text:", text)
    assert "Typos" in page.locator("h3").inner_text()

def test_text_extraction(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_text_extraction()
