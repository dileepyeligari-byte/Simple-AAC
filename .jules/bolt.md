
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-03-30 - DOM Repaints: Node Creation vs Visibility Toggling
**Learning:** Rebuilding DOM elements dynamically on search/filter using `innerHTML = ''` or `document.createElement` forces the browser to recompute styles and reflow the entire tree. For lists whose underlying data doesn't frequently change, building the DOM once and toggling node visibility via `style.display = 'none'` is exponentially faster since the nodes are already initialized in memory.
**Action:** When filtering or swapping views over an existing dataset, build all nodes initially and use CSS `display` toggling rather than adding/removing elements from the document. To handle underlying data updates (like edits or syncs), introduce dirty flags to force a single, explicit rebuilding pass.
