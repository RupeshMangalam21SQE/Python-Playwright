from playwright.sync_api import sync_playwright, expect

def _edit_iframe_content(page, text: str):
    page.goto("https://the-internet.herokuapp.com/iframe")

    frame = page.frame_locator("#mce_0_ifr")
    editor = frame.locator("#tinymce")

    editor.fill(text)

def test_iframe_interaction(page=None):
    if page: 
        _edit_iframe_content(page, "Hello from Playwright!")
        expect(page.frame_locator("#mce_0_ifr").locator("#tinymce")).to_have_text("Hello from Playwright!")

    else: 
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            iframe_page = chromium_browser.new_page()

            _edit_iframe_content(iframe_page, "Hello from Playwright!")
            expect(iframe_page.frame_locator("#mce_0_ifr").locator("#tinymce")).to_have_text("Hello from Playwright!")

            chromium_browser.close()

if __name__ == "__main__":
    test_iframe_interaction()
