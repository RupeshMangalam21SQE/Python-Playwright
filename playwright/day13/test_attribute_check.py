from playwright.sync_api import sync_playwright, expect

def _get_github_ribbon_image(page):
    page.goto("https://the-internet.herokuapp.com/")
    return page.locator("img").first

def test_attribute_check(page=None):
    if page:
        image = _get_github_ribbon_image(page)
        expect(image).to_have_attribute("src", "/img/forkme_right_green_007200.png")
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            homepage = chromium_browser.new_page()

            image = _get_github_ribbon_image(homepage)
            expect(image).to_have_attribute("src", "/img/forkme_right_green_007200.png")

            chromium_browser.close()

if __name__ == "__main__":
    test_attribute_check()
