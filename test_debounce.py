from playwright.sync_api import sync_playwright

def run_test(page):
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

    # 3. Type into the search input rapidly
    print("Typing 'apple' rapidly into search box...")
    search_box = page.get_by_label("Card Management (Filter/Search):")
    for char in "apple":
        search_box.press(char)
        page.wait_for_timeout(20) # Simulate fast typing without waiting for debounce

    # Wait for debounce to finish (300ms + some buffer)
    page.wait_for_timeout(500)

    # Verify the results are filtered
    cards = page.locator(".manage-item:visible").all()
    print(f"Number of cards displayed after search: {len(cards)}")

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
            run_test(page)
        finally:
            context.close()  # MUST close context to save the video
            browser.close()