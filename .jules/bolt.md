
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-04-03 - DOM Rebuilding vs Visibility Toggling
**Learning:** Destroying and recreating entire lists of DOM nodes (using `innerHTML = ''` and regenerating the fragment) for filtering is an expensive operation that forces complete layout recalculations.
**Action:** For frequently filtered grid/list components, generate the DOM nodes once and cache them. Update their visibility using `style.display = 'none'` or `''` based on dataset attribute checks. Only invalidate the cache (and rebuild nodes) when underlying data changes.