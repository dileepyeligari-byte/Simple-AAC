
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).
## 2026-04-18 - DOM Visibility Toggling During Filtering\n**Learning:** Rebuilding the DOM (destroying and recreating all child nodes) on every category filter click is expensive and causes layout thrashing. Hiding elements via `display: none` is much faster.\n**Action:** Render all grid nodes once using a DocumentFragment, then iterate and toggle `style.display = 'none'` based on filter logic. Use a boolean flag (like `gridNeedsRebuild`) to explicitly invalidate and rebuild the DOM cache only when underlying data (like language or level) changes.
