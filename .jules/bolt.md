
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2026-04-02 - DOM Reuse vs Node Recreation
**Learning:** Recreating DOM nodes (using `innerHTML = ''` followed by creating and appending new elements) on every search or filter is expensive and blocks the main thread with garbage collection and layout calculations. Toggling `style.display = 'none'` on pre-existing nodes is significantly faster.
**Action:** For lists and grids that change frequently via filtering or search, render all nodes once and use CSS display toggling to show/hide items instead of destroying and recreating DOM nodes.
