from playwright.sync_api import sync_playwright, expect

def _mock_dynamic_content(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.click("button")

    # Wait until the h4 exists (even if hidden)
    page.wait_for_selector("#finish h4")

    page.locator("#finish h4").evaluate("""el => el.textContent = "Mocked Hello World!" """)

def test_mocking_slow_api(page=None):
    if page:  
        _mock_dynamic_content(page)
        expect(page.locator("#finish h4")).to_have_text("Mocked Hello World!")
    else: 
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            dynamic_page = chromium_browser.new_page()

            _mock_dynamic_content(dynamic_page)
            expect(dynamic_page.locator("#finish h4")).to_have_text("Mocked Hello World!")

            chromium_browser.close()

if __name__ == "__main__":
    test_mocking_slow_api()
