
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-03-29 - DOM Visibility Toggling Indexing
**Learning:** When conditionally rendering DOM nodes to later toggle their visibility with `display: none`, you MUST render ALL nodes unconditionally during the initial fragment construction. Conditionally skipping nodes during initial render breaks the index alignment between the DOM children array (`grid.children`) and the underlying data array (`allCards`), causing the wrong items to be displayed during subsequent visibility updates.
**Action:** Always render 100% of the dataset into the DOM when using the caching/visibility pattern, and let the initial visibility iteration handle the hiding of elements that shouldn't be seen yet.
