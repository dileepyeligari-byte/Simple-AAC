## 2024-05-24 - Interactive Elements Need Keyboard Support
**Learning:** Custom interactive elements (like the AAC cards rendered as `div`s) must explicitly implement keyboard support (`role="button"`, `tabindex="0"`, and `keydown` event listeners for Enter/Space keys) to be accessible for users who rely on switch controls or keyboard navigation.
**Action:** Always add keyboard accessibility attributes and event listeners when using non-semantic HTML elements for interactivity.
## 2024-05-24 - Action buttons and toast accessibility
**Learning:** Action buttons should visually convey when they are unavailable (disabled state) to prevent confusion. Toast containers must use aria-live regions so screen readers can announce dynamic updates without requiring focus.
**Action:** Add disabled attributes to buttons that require state (e.g., non-empty input/selections), along with visual styles (opacity, cursor). Always add aria-live="polite" to global toast or notification containers.
## 2024-04-10 - Keyboard Accessible Hold-To-Unlock UX Pattern
**Learning:** For custom "hold-to-unlock" interactions like a secure Parent Gate FAB button, relying solely on pointer events (`mousedown`, `touchstart`, etc.) excludes keyboard users.
**Action:** Implement keyboard support explicitly by capturing `keydown` (checking `!event.repeat` to prevent instant trigger) and `keyup` for Enter or Space keys, pairing them with the respective start and stop functions used for pointer events.
