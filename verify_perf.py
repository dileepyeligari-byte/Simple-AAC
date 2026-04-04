from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Navigate to the local server
    page.goto("http://localhost:8000/index.html")
    page.wait_for_timeout(1000)

    # 1. Fill initialization modal (if present)
    try:
        page.get_by_label("Child's Name (English)").fill("Test Child")
        page.wait_for_timeout(500)
        page.get_by_label("Child's Name (Telugu)").fill("టెస్ట్ చైల్డ్")
        page.wait_for_timeout(500)
        page.get_by_role("button", name="Start Using AAC").click()
        page.wait_for_timeout(1000)
    except Exception as e:
        print("Init modal not found or already filled", e)

    # 2. Test Category Filters (loadCards)
    page.get_by_role("button", name="Needs").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Emotions").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="All").click()
    page.wait_for_timeout(1000)

    # 3. Open Admin Modal
    # The fab button has a mousedown/touchstart gate of 2 seconds
    fab = page.get_by_label("Parent Settings")
    fab.evaluate("el => { const event = new MouseEvent('mousedown'); el.dispatchEvent(event); }")
    page.wait_for_timeout(2500) # Wait for gate timer

    # 4. Test Search/Filter (loadAdminList)
    page.get_by_label("Learning Level:").select_option("5")
    page.wait_for_timeout(500)

    page.get_by_label("Card Management (Filter/Search):").fill("apple")
    page.wait_for_timeout(1000)

    page.get_by_label("Card Management (Filter/Search):").fill("")
    page.wait_for_timeout(1000)

    page.get_by_label("Card Management (Filter/Search):").fill("water")
    page.wait_for_timeout(1000)

    # Take screenshot
    page.screenshot(path="verification_perf.png")
    page.wait_for_timeout(1000)  # Hold final state for the video

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()  # MUST close context to save the video
            browser.close()