from playwright.sync_api import expect

class SearchComponent:
    def __init__(self, page):
        self.page = page
        self.search_input = "#search"
        self.search_button = "#search-btn"

    def search(self, query: str):
        self.page.fill(self.search_input, query)
        self.page.click(self.search_button)

    def verify_results(self, expected_text: str):
        expect(self.page.locator("#results")).to_contain_text(expected_text)
