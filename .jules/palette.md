## 2024-10-24 - Explicit Form Labeling
**Learning:** Found that custom settings and admin form inputs lacked explicit label associations (`for` linking to `id`) and standalone inputs lacked `aria-label`s. This is an accessibility barrier for screen readers trying to understand the configuration interface.
**Action:** When creating forms or interactive management lists in this app, explicitly use `for="[id]"` on `<label>` elements or `aria-label` for inputs without direct visual text labels.
