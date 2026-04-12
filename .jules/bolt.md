
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-05-13 - DOM Visibility Toggling vs Rebuilding
**Learning:** Destroying (`innerHTML = ''`) and recreating DOM nodes on every search or filter action is expensive (O(n)). Toggling `style.display` on existing cached elements is far more performant. However, when implementing this pattern, you *must* unconditionally render all possible nodes during the initial build phase. If you conditionally skip nodes during the first render, the underlying data array index will no longer match the `children` array index in the DOM, causing incorrect elements to be toggled later.
**Action:** Always render nodes unconditionally during the initial DOM construction when using the DOM visibility toggling pattern. Do not conditionally skip elements during the initial render.
