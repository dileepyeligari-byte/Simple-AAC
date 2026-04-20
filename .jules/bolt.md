
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).
## 2024-03-31 - DOM Nodes Visibility Toggling
**Learning:** During DOM generation for filtered data, if you conditionally skip element render during the initial pass, it can create a misalignment with array indexing later when using visibility toggling logic.
**Action:** When applying the DOM visibility toggling pattern (`style.display = 'none'`), render all nodes unconditionally during the initial DOM construction. Do not conditionally skip elements during the initial render.
