## 2024-05-24 - Interactive Elements Need Keyboard Support
**Learning:** Custom interactive elements (like the AAC cards rendered as `div`s) must explicitly implement keyboard support (`role="button"`, `tabindex="0"`, and `keydown` event listeners for Enter/Space keys) to be accessible for users who rely on switch controls or keyboard navigation.
**Action:** Always add keyboard accessibility attributes and event listeners when using non-semantic HTML elements for interactivity.
## 2024-05-24 - Action buttons and toast accessibility
**Learning:** Action buttons should visually convey when they are unavailable (disabled state) to prevent confusion. Toast containers must use aria-live regions so screen readers can announce dynamic updates without requiring focus.
**Action:** Add disabled attributes to buttons that require state (e.g., non-empty input/selections), along with visual styles (opacity, cursor). Always add aria-live="polite" to global toast or notification containers.
## 2024-05-18 - Global Focus Visible Pattern
**Learning:** Using `*:focus-visible` instead of targeting specific classes (like `.card:focus-visible`) is a much cleaner and more robust pattern for ensuring keyboard accessibility across an entire application. It establishes a global baseline, ensuring no interactive element is left without a focus indicator.
**Action:** Default to using global `*:focus-visible` rules for keyboard focus indicators rather than component-specific rules unless component-specific styling is strictly necessary.
