from playwright.sync_api import sync_playwright
import os
import glob

def run_cuj(page):
    page.goto("http://localhost:8000/index.html")
    page.wait_for_timeout(500)

    # Test Focus Visibility (Step 1)
    page.focus(".filter-chip.people")
    page.wait_for_timeout(500)

    page.focus("#btn-undo")
    page.wait_for_timeout(500)

    # Test FAB Keyboard Accessibility (Step 2)
    page.focus("#adminBtn")
    page.wait_for_timeout(500)

    # Hold Space to trigger the gate
    page.keyboard.down(" ")
    page.wait_for_timeout(2500) # Wait for 2s gate timer + buffer
    page.keyboard.up(" ")

    # Wait for the modal to be visible
    page.wait_for_selector("#admin-modal", state="visible", timeout=5000)
    page.wait_for_timeout(500)

    # Take screenshot of the open modal
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    # Clean old videos
    for f in glob.glob("/home/jules/verification/videos/*"):
        os.remove(f)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()  # MUST close context to save the video
            browser.close()
