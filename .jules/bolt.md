
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).
## 2026-04-14 - DOM Toggling Reflow Pattern

**Learning:** When using DOM visibility toggling (`style.display = 'none'`) for performance, you must invalidate and rebuild the cached DOM nodes whenever underlying data updates (e.g., using boolean rebuild flags like `needsGridRebuild` that are set to true on data changes like edits or language switches). Otherwise, the UI will reflect stale data. Also, ensure the test suite is updated to select `:visible` elements to avoid failures when testing pages using this pattern.
**Action:** Use boolean cache flags (`needsRebuild`) to invalidate and rebuild the DOM cache alongside state updates when implementing the visibility toggling pattern.
