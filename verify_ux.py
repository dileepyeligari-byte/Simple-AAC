import asyncio
from playwright.async_api import async_playwright

async def verify_focus_styles():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(record_video_dir="/home/jules/verification/")
        page = await context.new_page()

        await page.goto("http://localhost:8000/index.html")
        await page.wait_for_load_state("networkidle")

        # Test focus on a filter chip
        await page.focus(".filter-chip.people")
        await page.screenshot(path="/home/jules/verification/focus_filter.png")

        # Test focus on a button
        await page.focus("#btn-undo")
        await page.screenshot(path="/home/jules/verification/focus_undo.png")

        # Test focus on FAB
        await page.focus("#adminBtn")
        await page.screenshot(path="/home/jules/verification/focus_fab.png")

        # Test FAB hold-to-unlock via keyboard (Space)
        await page.keyboard.down(" ")
        await page.wait_for_timeout(2500) # Wait for gate timer
        await page.keyboard.up(" ")
        await page.wait_for_selector("#admin-modal", state="visible")
        await page.screenshot(path="/home/jules/verification/fab_unlocked.png")

        await context.close()
        await browser.close()

asyncio.run(verify_focus_styles())
