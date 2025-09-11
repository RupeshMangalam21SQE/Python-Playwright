from playwright.sync_api import sync_playwright, expect

def _press_key(page, key: str = "A"):
    page.goto("https://the-internet.herokuapp.com/key_presses")
    input_box = page.locator("#target")
    input_box.press(key)
    return page.locator("#result")

def test_keyboard_actions(page=None):
    if page:
        result = _press_key(page, "A")
        expect(result).to_have_text("You entered: A")
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            keyboard_page = chromium_browser.new_page()

            result = _press_key(keyboard_page, "A")
            expect(result).to_have_text("You entered: A")

            chromium_browser.close()

if __name__ == "__main__":
    test_keyboard_actions()
