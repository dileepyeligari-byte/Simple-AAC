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

    # 2. Open Admin Modal
    # The fab button has a mousedown/touchstart gate of 2 seconds
    fab = page.get_by_label("Parent Settings")
    fab.evaluate("el => { const event = new MouseEvent('mousedown'); el.dispatchEvent(event); }")
    page.wait_for_timeout(2500) # Wait for gate timer

    # 3. Interact with newly labeled inputs in Admin Modal
    # Test Language Select
    page.get_by_label("Display Language:").select_option("en")
    page.wait_for_timeout(500)

    # Test Level Select
    page.get_by_label("Learning Level:").select_option("5")
    page.wait_for_timeout(500)

    # Test Card Management Search
    page.get_by_label("Card Management (Filter/Search):").fill("apple")
    page.wait_for_timeout(500)

    # Test Edit Card to see those labels
    # We find the edit button for the apple card
    page.locator("button[aria-label=\"Edit Card\"]:visible").first.click()
    page.wait_for_timeout(1000)

    # Test the aria-labels on the edit form
    page.get_by_label("English Text").fill("Apple Updated")
    page.wait_for_timeout(500)

    page.get_by_role("button", name="💾 Save Card").click()
    page.wait_for_timeout(1000)

    # Take screenshot at the key moment (Admin modal open)
    page.screenshot(path="verification.png")
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
