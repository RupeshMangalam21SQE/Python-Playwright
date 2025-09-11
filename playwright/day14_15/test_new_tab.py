from playwright.sync_api import sync_playwright, expect

def _open_new_tab(main_page):
    main_page.goto("https://the-internet.herokuapp.com/windows")
    with main_page.context.expect_page() as new_page_event:
        main_page.get_by_role("link", name="Click Here").click()
    new_tab = new_page_event.value
    new_tab.wait_for_load_state()
    return new_tab

def test_new_tab(page=None):
    if page:  
        new_tab = _open_new_tab(page)
        expect(new_tab).to_have_title("New Window")
    else:  
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            main_page = chromium_browser.new_page()

            new_tab = _open_new_tab(main_page)
            expect(new_tab).to_have_title("New Window")

            chromium_browser.close()

if __name__ == "__main__":
    test_new_tab()
