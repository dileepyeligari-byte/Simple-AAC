
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-05-24 - DOM Visibility Toggling Optimization
**Learning:** Destroying and recreating DOM nodes (`innerHTML = ''`) on every filter/search keystroke causes significant reflow bottlenecks, even with debouncing.
**Action:** When filtering frequently updated lists or grids, render all nodes unconditionally during the initial build and toggle `style.display = 'none'` on existing DOM nodes. Use explicit boolean flags to rebuild the DOM only when the underlying data structurally changes (e.g., edits or language switches).
