
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).
## 2024-04-14 - DOM Visibility Toggling
**Learning:** Using `innerHTML = ''` to clear and recreate DOM nodes frequently (e.g. during search or filtering) is a performance bottleneck due to excessive reflows and memory thrashing.
**Action:** When filtering a cached list of elements, render the nodes unconditionally once, and toggle visibility using `style.display = 'none' / 'flex'`. Use a rebuild flag (e.g., `domNeedsRebuild`) invalidated only when the underlying data changes to know when to rebuild the DOM.
