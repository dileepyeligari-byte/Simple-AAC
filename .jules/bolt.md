
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-05-18 - DOM Visibility Toggling vs Rebuilding
**Learning:** Rebuilding the DOM (`innerHTML = ''` followed by appending nodes) on every UI filter interaction (like switching categories or typing in a search bar) causes excessive layout thrashing and reflows. Caching DOM nodes and toggling `style.display = 'none'` is much faster but requires careful state management to ensure hidden DOM maps accurately to underlying data.
**Action:** When applying the DOM visibility toggling pattern, introduce a "dirty" state flag (e.g., `_domDirty = true`). Render the DOM once unconditionally when the flag is set. Then, separately iterate over the DOM children and toggle visibility. Invalidate this cache (set flag back to `true`) whenever the underlying source of truth data (e.g. from IndexedDB) mutates.
