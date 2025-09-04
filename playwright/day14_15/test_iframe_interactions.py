from playwright.sync_api import sync_playwright, expect
import pytest

def _run_test(page):
    # Go to iframe demo page
    page.goto("https://the-internet.herokuapp.com/iframe")

    # Get iframe
    frame = page.frame_locator("#mce_0_ifr")

    # Locate editable body inside iframe
    editor = frame.locator("#tinymce")

    # Clear old content (Ctrl+A + Delete)
    editor.click()
    editor.press("Control+A")
    editor.press("Delete")

    # Type new text
    editor.type("Hello from Playwright!")

    # Verify content
    expect(editor).to_have_text("Hello from Playwright!")

def test_iframe_interaction(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_iframe_interaction()
