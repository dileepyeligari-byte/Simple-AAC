## 2024-05-24 - Bulk IndexedDB Data Retrieval Optimization
**Learning:** Using `store.openCursor()` for bulk data retrieval in IndexedDB fires a separate `onsuccess` event for every single record, creating significant event loop overhead and slowing down rendering.
**Action:** Always prefer `store.getAll()` over `openCursor()` when retrieving an entire object store's contents to fetch data in a single event loop tick, which dramatically improves load performance for PWAs.
