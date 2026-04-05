
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-05-20 - DOM Visibility Toggling
**Learning:** When applying the DOM visibility toggling pattern (`style.display = 'none'`), unconditionally render all nodes during the initial DOM construction. Conditionally skipping elements causes index mismatches between the underlying data array and DOM children when iterating to toggle visibility later. Playwright also needs to explicitly locate using the `:visible` pseudo-class (e.g., `locator('.item:visible')`) to correctly interact with and count elements under this pattern.
**Action:** Always render nodes 1:1 with the data array on the first pass, then iterate and toggle `display: none` based on filter logic.
