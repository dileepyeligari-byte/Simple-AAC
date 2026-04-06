
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-05-18 - DOM Caching and Conditional Rebuilding for Filters
**Learning:** Destroying and recreating DOM nodes (`innerHTML = ''`) for frequently updated views like category filtering is slow and causes reflows. Caching DOM nodes and toggling `style.display` is much faster. However, the DOM cache must be explicitly invalidated and rebuilt when underlying data changes (e.g., card edits, additions, deletions, or language toggles), otherwise the UI shows stale data or incorrect labels.
**Action:** When implementing DOM caching for filters, render all nodes unconditionally during the initial build to avoid index/data mismatches later. Add a `forceRebuild` parameter to the rendering function and pass `true` on any data-mutating action or language switch to invalidate the cache. Pass `false` for pure visual filtering.
