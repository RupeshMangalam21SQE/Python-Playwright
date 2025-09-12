from playwright.sync_api import sync_playwright, expect
import time

def _run_debug_trace_demo(page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    # This element does NOT exist – intentional failure for trace demo
    expect(page.locator("#does-not-exist")).to_be_visible(timeout=3000)

def test_debug_trace(page=None):
    if page:
        _run_debug_trace_demo(page)
    else:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False, slow_mo=500)
            context = browser.new_context()

            # Start tracing
            context.tracing.start(screenshots=True, snapshots=True, sources=True)

            page = context.new_page()
            try:
                _run_debug_trace_demo(page)
            finally:
                # Save trace with timestamp
                trace_path = f"trace-{int(time.time())}.zip"
                context.tracing.stop(path=trace_path)
                print(f"Trace saved to {trace_path}")
                browser.close()

if __name__ == "__main__":
    test_debug_trace()
