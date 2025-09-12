import pytest
from playwright.async_api import expect
from config import URLS

@pytest.mark.regression
@pytest.mark.asyncio
async def test_dynamic_loading(page):
    await page.goto(URLS["dynamic_loading"])
    await page.click("button")

    await expect(page.locator("#loading")).to_be_hidden(timeout=10000)
    await expect(page.locator("#finish")).to_be_visible(timeout=10000)
    await expect(page.locator("#finish h4")).to_have_text("Hello World!", timeout=10000)
