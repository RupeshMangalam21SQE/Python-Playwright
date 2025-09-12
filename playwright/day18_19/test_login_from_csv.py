import csv
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright, expect

def read_csv():
    """Read test data from credentials.csv"""
    file_path = Path(__file__).parent / "credentials.csv"
    with open(file_path, newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
        # If header detected (starts with 'username'), skip it
        if rows and rows[0][0].lower() == "username":
            rows = rows[1:]
        return rows

def _run_test(page, username, password, expected_text):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", username)
    page.fill("#password", password)
    page.click("button[type='submit']")
    flash = page.locator("#flash")
    expect(flash).to_contain_text(expected_text)

@pytest.mark.parametrize("username,password,expected_text", read_csv())
def test_login_from_csv(username, password, expected_text, page):
    _run_test(page, username, password, expected_text)

if __name__ == "__main__":
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()

        for username, password, expected in read_csv():
            page = context.new_page()
            print(f"Testing with: {username}/{password}")
            _run_test(page, username, password, expected)
            page.close()

        browser.close()
