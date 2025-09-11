from playwright.sync_api import sync_playwright, expect

def _hover_first_figure(page):
    page.goto("https://the-internet.herokuapp.com/hovers")
    figure = page.locator(".figure").first
    figure.hover()
    return figure.locator(".figcaption h5")

def test_hover_and_click(page=None):
    if page:
        caption = _hover_first_figure(page)
        expect(caption).to_be_visible()
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            hover_page = chromium_browser.new_page()

            caption = _hover_first_figure(hover_page)
            expect(caption).to_be_visible()

            chromium_browser.close()

if __name__ == "__main__":
    test_hover_and_click()
