
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).
## 2026-04-13 - DOM Thrashing in UI Filters
**Learning:** Frequent array iteration that destroys and recreates DOM nodes (`innerHTML = ''`) upon simple input changes (like search filtering or category switching) causes significant UI blocking and rendering jank.
**Action:** When filtering a static or rarely-changing list, render all nodes unconditionally and toggle visibility via `style.display = 'none'` or `style.display = ''`. Pair this with a boolean dirty flag (e.g., `needRebuild = true`) triggered only on actual data mutations (like saving or deleting a card) to invalidate and fully rebuild the cached DOM nodes when necessary.
