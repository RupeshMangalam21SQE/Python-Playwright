from playwright.sync_api import sync_playwright, expect
import pytest

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/windows")
    with page.context.expect_page() as new_page_event:
        page.get_by_role("link", name="Click Here").click()
    new_page = new_page_event.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_title("New Window")

def test_new_tab(page=None):
    if page:  # pytest run
        _run_test(page)
    else:  # direct run
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_new_tab()
