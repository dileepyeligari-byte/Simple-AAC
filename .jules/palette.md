## 2024-05-24 - Interactive Elements Need Keyboard Support
**Learning:** Custom interactive elements (like the AAC cards rendered as `div`s) must explicitly implement keyboard support (`role="button"`, `tabindex="0"`, and `keydown` event listeners for Enter/Space keys) to be accessible for users who rely on switch controls or keyboard navigation.
**Action:** Always add keyboard accessibility attributes and event listeners when using non-semantic HTML elements for interactivity.
## 2024-05-24 - Action buttons and toast accessibility
**Learning:** Action buttons should visually convey when they are unavailable (disabled state) to prevent confusion. Toast containers must use aria-live regions so screen readers can announce dynamic updates without requiring focus.
**Action:** Add disabled attributes to buttons that require state (e.g., non-empty input/selections), along with visual styles (opacity, cursor). Always add aria-live="polite" to global toast or notification containers.

## 2024-05-15 - Modal Dialog Accessibility
**Learning:** In custom modal implementations, it is critical to include `role="dialog"`, `aria-modal="true"`, and `aria-labelledby`/`aria-describedby` attributes on the modal container to ensure screen readers correctly announce the modal and trap virtual focus.
**Action:** Always apply these ARIA attributes to modal overlays/containers, referencing the modal's internal title and description elements.
