from playwright.sync_api import sync_playwright, expect

def _trigger_confirm_dialog(page, action: str):
    if action == "accept":
        page.once("dialog", lambda dialog: dialog.accept())
    elif action == "dismiss":
        page.once("dialog", lambda dialog: dialog.dismiss())
    else:
        raise ValueError(f"Unsupported action: {action}")

    page.get_by_role("button", name="Click for JS Confirm").click()

def test_confirm_dialog(page=None):
    if page:  
        _trigger_confirm_dialog(page, "accept")
        expect(page.locator("#result")).to_have_text("You clicked: Ok")

        _trigger_confirm_dialog(page, "dismiss")
        expect(page.locator("#result")).to_have_text("You clicked: Cancel")

    else: 
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            confirm_page = chromium_browser.new_page()

            _trigger_confirm_dialog(confirm_page, "accept")
            expect(confirm_page.locator("#result")).to_have_text("You clicked: Ok")

            _trigger_confirm_dialog(confirm_page, "dismiss")
            expect(confirm_page.locator("#result")).to_have_text("You clicked: Cancel")

            chromium_browser.close()

if __name__ == "__main__":
    test_confirm_dialog()
