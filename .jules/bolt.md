
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-05-18 - Fast DOM Filtering via Visibility Toggling
**Learning:** Even when `IndexedDB` reads are fast (`getAll()`), completely tearing down (`innerHTML = ''`) and recreating large DOM lists on every filter click causes noticeable UI layout thrashing.
**Action:** Instead of recreating the DOM for filtering, render all items unconditionally once and store the data array. On subsequent filter actions, bypass the database, iterate over the cached array alongside the `grid.children`, and apply `style.display = 'none'` or `''` to toggle visibility. Explicitly cache invalidate (re-fetch/re-render) only when the underlying data mutates (adds, edits, deletes, or language changes).
