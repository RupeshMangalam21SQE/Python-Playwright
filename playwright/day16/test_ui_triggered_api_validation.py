from playwright.sync_api import sync_playwright, expect

def _submit_contact_form(page, api_context, form_data):
    page.goto("https://www.webdriveruniversity.com/Contact-Us/contactus.html")

    page.fill("input[name='first_name']", form_data["first_name"])
    page.fill("input[name='last_name']", form_data["last_name"])
    page.fill("input[name='email']", form_data["email"])
    page.fill("textarea[name='message']", form_data["message"])

    page.click("input[value='SUBMIT']")

    response = api_context.post(
        "https://httpbin.org/post",
        form=form_data
    )

    return response

def test_ui_triggered_api_validation(page=None):
    form_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "message": "Hello, this is a test message."
    }

    with sync_playwright() as playwright:
        api_context = playwright.request.new_context()

        if page:
            contact_page = page
        else:
            chromium_browser = playwright.chromium.launch(headless=False)
            contact_page = chromium_browser.new_page()

        response = _submit_contact_form(contact_page, api_context, form_data)

        expect(contact_page.locator("body")).to_contain_text("Thank You for your Message!")

        assert response.ok, f"API call failed: {response.status}"
        result = response.json()
        assert result["form"]["first_name"] == form_data["first_name"]
        assert result["form"]["email"] == form_data["email"]
        print("API validation successful")
        print(result)

        if not page:
            chromium_browser.close()

if __name__ == "__main__":
    test_ui_triggered_api_validation()
