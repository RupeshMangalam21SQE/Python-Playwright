from playwright.sync_api import sync_playwright, expect

def _trigger_js_alert(page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()

def test_alert_handling(page=None):
    if page:
        _trigger_js_alert(page)

        expect(page.locator("#result")).to_have_text("You successfully clicked an alert")

    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            alert_page = chromium_browser.new_page()

            _trigger_js_alert(alert_page)

            expect(alert_page.locator("#result")).to_have_text("You successfully clicked an alert")

            chromium_browser.close()

if __name__ == "__main__":
    test_alert_handling()
