## 2024-05-18 - Missing ARIA labels pattern
**Learning:** This app heavily uses icon-only buttons (like Erase Last, Clear Everything, Parent Settings FAB, and dynamically created Edit/Delete buttons) without accompanying ARIA labels, creating accessibility issues for screen reader users.
**Action:** When working on this application, always review icon-only buttons and dynamically created elements in the admin modal to ensure they have descriptive `aria-label` attributes.
