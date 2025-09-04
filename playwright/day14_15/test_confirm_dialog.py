from playwright.sync_api import sync_playwright, expect
import pytest

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    # Accept confirm
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.locator("#result")).to_have_text("You clicked: Ok")

    # Dismiss confirm
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")

def test_confirm_dialog(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_confirm_dialog()
