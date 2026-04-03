
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-04-03 - DOM Node Creation vs Visibility Toggling
**Learning:** Frequent clearing (`innerHTML = ''`) and rebuilding of DOM nodes during search or filtering operations causes severe layout thrashing and slows down UI responsiveness.
**Action:** When filtering frequently updated lists or grids, render all elements to the DOM unconditionally once. On subsequent filter events, iterate over the existing elements and toggle their CSS `style.display` property (`''` or `'none'`) instead of destroying and recreating them. Ensure any test scripts selecting elements account for invisible DOM nodes (e.g., using `:visible` pseudo-class in locators). When applying the visibility toggle pattern, always build the entire DOM set initially to prevent mapping issues.
