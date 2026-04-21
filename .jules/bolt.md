
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-03-29 - DOM Visibility Toggling vs Rebuilding
**Learning:** Destroying and recreating DOM nodes (`innerHTML = ''` + `appendChild`) on every search keystroke or category filter change is highly inefficient and causes layout thrashing, even with DocumentFragment batching.
**Action:** Implement a visibility toggling pattern (`style.display = 'none'`). Render DOM nodes exactly once, maintain parity between the underlying data array and `container.children`, and only loop to update `style.display`. Use rebuild flags to completely recreate nodes only when the underlying dataset physically changes (e.g., database edits or language swaps). When implementing, target `:visible` elements in Playwright tests to avoid test regressions.
