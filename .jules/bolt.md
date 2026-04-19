
## 2024-03-29 - IndexedDB Data Retrieval: openCursor vs getAll
**Learning:** Using `openCursor()` for bulk data retrieval in IndexedDB (like loading a full list of cards) has high callback overhead because it triggers an event for every single row. Using `getAll()` executes much faster natively by returning all matching records in a single callback, minimizing event loop interactions.
**Action:** Replace `openCursor()` loops with `getAll()` when retrieving entire object stores or indexes where memory permits, especially during initial data loads or cache syncs.

## 2024-03-29 - Search Input Debouncing
**Learning:** Filtering cached arrays and batching DOM insertions is good, but doing it synchronously on every keystroke without debouncing is a bottleneck that causes UI jank.
**Action:** Debounce high-frequency inputs (like search bars) that trigger DOM rebuilds, even when data retrieval is O(1).

## 2024-03-31 - DOM Visibility Toggling for Filtering
**Learning:** Destroying and recreating the entire DOM grid (`grid.innerHTML = ''`) on every category filter change is computationally expensive, causes unnecessary reflows, and drops existing scroll positions or states.
**Action:** Render all items unconditionally once and use a cached flag (`needsRebuild`). When the underlying dataset changes (e.g., adding/editing a card or changing the global language state), set `needsRebuild = true` to force a complete DOM recreation. For transient UI interactions like filtering, set the display property of existing cached DOM nodes (`child.style.display = 'none' or 'flex'`) to bypass the costly DOM insertion phase.
