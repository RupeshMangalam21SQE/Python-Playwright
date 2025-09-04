from playwright.sync_api import sync_playwright, expect
import pytest

def _run_test(page):
    # Step 1: Go to page A
    page.goto("https://the-internet.herokuapp.com/windows")

    # Step 2: Open page B in a new tab
    with page.context.expect_page() as new_page_event:
        page.get_by_role("link", name="Click Here").click()
    new_page = new_page_event.value
    new_page.wait_for_load_state()

    # Step 3: Grab text from page B
    text = new_page.locator("h3").inner_text()
    new_page.close()

    # Step 4: Go to login page and paste text
    page.goto("https://the-internet.herokuapp.com/login")
    input_box = page.locator("#username")
    input_box.fill(text)

    # Step 5: Verify the value
    expect(input_box).to_have_value(text)

def test_multi_window_workflow(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_multi_window_workflow()
