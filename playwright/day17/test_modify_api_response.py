from playwright.sync_api import sync_playwright, expect

MOCK_PRODUCTS_JSON = '{"products":[{"id":1,"name":"Modified Product"}]}'

def _run_test(page):
    # Intercept and modify /products response
    def mock_products_response(route, request):
        route.fulfill(
            status=200,
            content_type="application/json",
            body=MOCK_PRODUCTS_JSON,
        )

    page.route("**/products", mock_products_response)

    # Inject a UI that fetches products
    page.set_content("""
        <ul id="products"></ul>
        <script>
        fetch("http://localhost/products")
          .then(r => r.json())
          .then(data => {
              document.querySelector("#products").innerHTML =
                data.products.map(p => `<li>${p.name}</li>`).join("");
          });
        </script>
    """)

    # Assert rendered UI
    items = page.locator("li")
    expect(items).to_have_count(1)
    expect(items).to_have_text("Modified Product")

def test_mock_products_api(page=None):
    if page: 
        _run_test(page)
    else:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            test_page = browser.new_page()
            _run_test(test_page)
            browser.close()

if __name__ == "__main__":
    test_mock_products_api()
