
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-03-29 - DOM Rendering: Visibility Toggling vs Rebuilding
**Learning:** Destroying and recreating DOM nodes (`innerHTML = ''` followed by re-appending) for frequent list filtering (like search bars or category chips) causes significant layout thrashing and reflow bottlenecks. Toggling `style.display = 'none'` is dramatically faster but requires maintaining a strict 1:1 index relationship between the underlying data array and the DOM children during the initial render. If you conditionally skip elements during the initial render, index-based toggling (`grid.children[i]`) will fail.
**Action:** When optimizing lists for frequent filtering, unconditionally render ALL nodes once, cache them, and then iterate through the array/DOM children to toggle visibility. Introduce an explicit invalidation flag (e.g., `domInvalidated = true`) to trigger a full rebuild only when the underlying data is actually added, removed, or modified.
