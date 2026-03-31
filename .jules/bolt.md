## 2024-05-24 - IndexedDB openCursor() vs getAll()
**Learning:** `openCursor()` fires a success event for every single record, creating massive event loop overhead when retrieving the entire dataset.
**Action:** Always prefer `getAll()` over `openCursor()` for bulk IndexedDB data retrieval to minimize event loop overhead and reduce main thread blocking.