from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/key_presses")
    input_box = page.locator("#target")
    input_box.press("A")
    result = page.locator("#result")
    expect(result).to_have_text("You entered: A")

def test_keyboard_actions(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_keyboard_actions()
