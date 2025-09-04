import asyncio
from playwright.async_api import async_playwright, expect

async def _run_test(page):
    await page.goto("https://playwright.dev/")
    await expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

async def async_main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await _run_test(page)
        await browser.close()

def test_async_script():
    asyncio.run(async_main())

if __name__ == "__main__":
    test_async_script()
