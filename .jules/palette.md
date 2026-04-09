## 2024-05-24 - Interactive Elements Need Keyboard Support
**Learning:** Custom interactive elements (like the AAC cards rendered as `div`s) must explicitly implement keyboard support (`role="button"`, `tabindex="0"`, and `keydown` event listeners for Enter/Space keys) to be accessible for users who rely on switch controls or keyboard navigation.
**Action:** Always add keyboard accessibility attributes and event listeners when using non-semantic HTML elements for interactivity.
## 2024-05-24 - Action buttons and toast accessibility
**Learning:** Action buttons should visually convey when they are unavailable (disabled state) to prevent confusion. Toast containers must use aria-live regions so screen readers can announce dynamic updates without requiring focus.
**Action:** Add disabled attributes to buttons that require state (e.g., non-empty input/selections), along with visual styles (opacity, cursor). Always add aria-live="polite" to global toast or notification containers.

## 2024-05-18 - Global Focus and Modal Accessibility
**Learning:** Found that custom modal implementations often lack ARIA roles (`role="dialog"`, `aria-modal="true"`), and focus rings were restricted only to specific interactive elements (`.card`) rather than all interactive elements, leading to poor keyboard navigation visibility.
**Action:** Always apply `*:focus-visible` globally for consistent keyboard navigation outlines, and explicitly add `role="dialog"` and `aria-modal="true"` to any custom modal containers.
