
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-03-29 - DOM Visibility Toggling for List Filtering
**Learning:** For frequently updated lists or grids (like search filtering), constantly destroying and recreating DOM nodes (`innerHTML = ''`) is a major performance bottleneck, especially in vanilla JS without virtual DOM differencing. Rendering nodes once and toggling visibility (`style.display = 'none'`) is significantly faster.
**Action:** When implementing list filtering in vanilla PWAs, unconditionally render all underlying array data to the DOM once and use a rebuild flag (`needsRebuild = false`). Then iterate through the cached DOM nodes and apply `style.display = match ? '' : 'none'` for subsequent filtering. Ensure the rebuild flag is set back to `true` whenever the underlying data changes.
