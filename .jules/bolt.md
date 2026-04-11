
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).
## 2024-04-11 - Playwright Visibility Locator Anti-Pattern
**Learning:** Playwright python test scripts fail when testing a page that uses CSS `display: none` to hide elements if they use `.filter(state="visible")` on a Locator object, or if they just use `.first` on a label query that matches multiple items (some hidden). Playwright's `Locator.first` does not automatically filter out hidden elements, and it hangs/fails trying to interact with the invisible first element.
**Action:** When filtering a locator to only visible elements in Playwright Python, strictly use the CSS pseudo-class `:visible` (e.g., `page.locator('[aria-label="Edit Card"]:visible').first`). Never use `.filter(state="visible")` and never call `.first.click()` on a query that might return hidden nodes.
