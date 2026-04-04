## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-04-04 - DOM Node Caching & Data Mutation Invalidation
**Learning:** Rendering DOM nodes once and toggling their visibility via CSS `display` is significantly faster than recreating nodes (`innerHTML = ''`), but simply checking if array lengths match is an insufficient cache invalidation strategy when editing data. The nodes must be forced to completely re-render whenever the underlying data structure's contents are mutated (e.g., edited texts, swapped emojis, or global language toggles).
**Action:** When implementing node caching with CSS `display` toggling, explicitly set rendering flags to `false` in the data synchronization function to guarantee that mutations force a fresh DOM build.
