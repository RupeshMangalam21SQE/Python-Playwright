from playwright.sync_api import sync_playwright, expect

def _run_test(page):
    # Use homepage instead of broken_images
    page.goto("https://the-internet.herokuapp.com/")

    # Locate the GitHub ribbon image
    image = page.locator("img").first
    expect(image).to_have_attribute("src", "/img/forkme_right_green_007200.png")

def test_attribute_check(page=None):
    if page:
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            _run_test(page)
            browser.close()
