
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).
## 2024-05-14 - DOM Visibility Toggling vs Rebuilding
**Learning:** In a vanilla JS app handling large lists (e.g., 60+ cards), dynamically destroying (`innerHTML = ''`) and recreating DOM nodes on every search keystroke or filter click causes noticeable reflow and repaints, especially on mobile devices.
**Action:** When implementing list filtering/search, render the full list to the DOM once unconditionally (controlled by a `needsRebuild` flag invalidated only when underlying data changes), and implement search/filtering by iterating over `element.children` and toggling `style.display = 'none'`. This O(n) traversal without DOM mutation is significantly faster than O(n) DOM element creation. Always ensure initial render includes all possible elements so array indices match DOM indices.
