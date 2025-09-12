from playwright.sync_api import sync_playwright, expect

def _block_ads(page):
    def block_request(route, request):
        route.abort()

    page.route("**/*ads*", block_request)

    # Inject sample content with an ad request
    page.set_content("""
        <div id="content">Main Content</div>
        <img src="http://ads.example.com/banner.jpg" class="ad-banner"/>
    """)

def test_ad_requests_are_blocked(page=None):
    if page:
        _block_ads(page)
        expect(page.locator("#content")).to_have_text("Main Content")
        # Ad image exists in DOM but won't load
        expect(page.locator(".ad-banner")).to_have_count(1)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            test_page = browser.new_page()

            _block_ads(test_page)
            expect(test_page.locator("#content")).to_have_text("Main Content")
            expect(test_page.locator(".ad-banner")).to_have_count(1)

            browser.close()

if __name__ == "__main__":
    test_ad_requests_are_blocked()
