# test_api_failure.py
from playwright.sync_api import sync_playwright, expect
from constants import ERROR_MESSAGE 


def _simulate_api_failure(page):
    def fail_route(route, request):
        route.fulfill(status=500, body="Internal Server Error")

    page.route("**/items", fail_route)

    page.set_content(f"""
        <div id="error"></div>
        <script>
        fetch("/items")
          .then(r => {{
              if (!r.ok) throw new Error("API failed");
              return r.json();
          }})
          .catch(() => {{
              document.querySelector("#error").innerText = "{ERROR_MESSAGE}";
          }});
        </script>
    """)


def test_api_error_state(page=None):
    if page:
        _simulate_api_failure(page)
        expect(page.locator("#error")).to_have_text(ERROR_MESSAGE)
    else:
        with sync_playwright() as playwright:
            chromium_browser = playwright.chromium.launch(headless=False)
            test_page = chromium_browser.new_page()

            _simulate_api_failure(test_page)
            expect(test_page.locator("#error")).to_have_text(ERROR_MESSAGE)

            chromium_browser.close()


if __name__ == "__main__":
    test_api_error_state()
