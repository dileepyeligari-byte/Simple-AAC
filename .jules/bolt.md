## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-03-29 - DOM Visibility Toggling
**Learning:** For frequently updated lists/grids (e.g., search filtering or category switching), destroying and recreating DOM nodes (`innerHTML = ''`) is expensive. Rendering nodes once unconditionally and toggling visibility (`style.display = 'none'`) is much faster. However, when doing so, never conditionally skip elements during the initial render as this causes index mismatches between the underlying data array and DOM children when iterating to toggle visibility.
**Action:** Render all nodes unconditionally during initial construction, and explicitly invalidate/rebuild the cached DOM nodes via boolean flags when underlying data changes (e.g., edits, deletes, or language switches), rather than relying on array length.
