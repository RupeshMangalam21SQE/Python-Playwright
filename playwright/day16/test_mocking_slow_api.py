from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    page.click("button")  # Start loading

    # Wait until the h4 exists (even if hidden)
    page.wait_for_selector("#finish h4")

    # Inject our mocked text
    page.evaluate("""() => {
        const finish = document.querySelector("#finish h4");
        if (finish) {
            finish.textContent = "Mocked Hello World!";
        }
    }""")

    # Verify mocked content
    expect(page.locator("#finish h4")).to_have_text("Mocked Hello World!")

def test_mocking_slow_api(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()

if __name__ == "__main__":
    test_mocking_slow_api()
