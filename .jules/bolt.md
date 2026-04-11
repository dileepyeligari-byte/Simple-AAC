
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-05-18 - Prevent Reflows with Visibility Toggling in Vanilla JS
**Learning:** In Vanilla JS applications, indiscriminately wiping (`innerHTML = ''`) and recreating large DOM lists on every filter/search keystroke causes excessive reflows and repaints, severely degrading performance.
**Action:** When filtering lists/grids in this codebase, use the Visibility Toggling pattern: establish a boolean flag (`needsRebuild = true`), reset it to true only on underlying data updates, unconditionally render *all* DOM nodes once when the flag is true to match the data array structure/indices exactly, and finally, loop over the children and toggle `style.display = 'none'` or `''` to apply the filter instead of destroying nodes.
