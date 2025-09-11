from playwright.sync_api import sync_playwright, expect

def _extract_typo_text(page):
    page.goto("https://the-internet.herokuapp.com/typos")
    return page.locator("div.example p").nth(1).inner_text()

def test_text_extraction(page=None):
    if page:
        extracted_text = _extract_typo_text(page)
        expect(page.locator("h3")).to_have_text("Typos")
        assert extracted_text is not None and len(extracted_text) > 0
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            typo_page = chromium_browser.new_page()

            extracted_text = _extract_typo_text(typo_page)

            expect(typo_page.locator("h3")).to_have_text("Typos")
            assert extracted_text is not None and len(extracted_text) > 0

            chromium_browser.close()

if __name__ == "__main__":
    test_text_extraction()
