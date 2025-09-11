import asyncio
from playwright.async_api import async_playwright, expect

async def _navigate_to_home(page):
    await page.goto("https://playwright.dev/")

async def async_main():
    async with async_playwright() as playwright:
        chromium_browser = await playwright.chromium.launch(headless=False)
        homepage = await chromium_browser.new_page()
        await _navigate_to_home(homepage)
        await expect(homepage).to_have_title(
            "Fast and reliable end-to-end testing for modern web apps | Playwright")
        await chromium_browser.close()

def test_async_script():
    asyncio.run(async_main())

if __name__ == "__main__":
    test_async_script()
