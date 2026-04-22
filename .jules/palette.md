## 2024-05-24 - Interactive Elements Need Keyboard Support
**Learning:** Custom interactive elements (like the AAC cards rendered as `div`s) must explicitly implement keyboard support (`role="button"`, `tabindex="0"`, and `keydown` event listeners for Enter/Space keys) to be accessible for users who rely on switch controls or keyboard navigation.
**Action:** Always add keyboard accessibility attributes and event listeners when using non-semantic HTML elements for interactivity.
## 2024-05-24 - Action buttons and toast accessibility
**Learning:** Action buttons should visually convey when they are unavailable (disabled state) to prevent confusion. Toast containers must use aria-live regions so screen readers can announce dynamic updates without requiring focus.
**Action:** Add disabled attributes to buttons that require state (e.g., non-empty input/selections), along with visual styles (opacity, cursor). Always add aria-live="polite" to global toast or notification containers.
## 2024-05-24 - Consistent Focus and Semantic Modals
**Learning:** Specific element focus styles (like `.card:focus-visible`) often leave other interactive elements (buttons, inputs) without clear keyboard navigation indicators. Modals lacking `role="dialog"`, `aria-modal="true"`, and `aria-labelledby`/`describedby` trap screen reader users without context.
**Action:** Use a global `*:focus-visible` rule (avoiding `border-radius: inherit;`) to ensure all interactive elements show focus consistently. Always ensure modal containers have semantic dialog attributes linking to their titles and descriptions.
