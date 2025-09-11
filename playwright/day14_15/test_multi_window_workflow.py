from playwright.sync_api import sync_playwright, expect

def _multi_window_workflow(main_page):
    main_page.goto("https://the-internet.herokuapp.com/windows")

    with main_page.context.expect_page() as new_page_event:
        main_page.get_by_role("link", name="Click Here").click()
    new_tab = new_page_event.value
    new_tab.wait_for_load_state()

    extracted_text = new_tab.locator("h3").inner_text()
    new_tab.close()

    main_page.goto("https://the-internet.herokuapp.com/login")
    input_box = main_page.locator("#username")
    input_box.fill(extracted_text)

    return input_box, extracted_text

def test_multi_window_workflow(page=None):
    if page:
        input_box, text_value = _multi_window_workflow(page)
        expect(input_box).to_have_value(text_value)
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            main_page = chromium_browser.new_page()

            input_box, text_value = _multi_window_workflow(main_page)
            expect(input_box).to_have_value(text_value)

            chromium_browser.close()

if __name__ == "__main__":
    test_multi_window_workflow()
