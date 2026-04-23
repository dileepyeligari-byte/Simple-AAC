## 2024-05-24 - Interactive Elements Need Keyboard Support
**Learning:** Custom interactive elements (like the AAC cards rendered as `div`s) must explicitly implement keyboard support (`role="button"`, `tabindex="0"`, and `keydown` event listeners for Enter/Space keys) to be accessible for users who rely on switch controls or keyboard navigation.
**Action:** Always add keyboard accessibility attributes and event listeners when using non-semantic HTML elements for interactivity.
## 2024-05-24 - Action buttons and toast accessibility
**Learning:** Action buttons should visually convey when they are unavailable (disabled state) to prevent confusion. Toast containers must use aria-live regions so screen readers can announce dynamic updates without requiring focus.
**Action:** Add disabled attributes to buttons that require state (e.g., non-empty input/selections), along with visual styles (opacity, cursor). Always add aria-live="polite" to global toast or notification containers.
## 2024-05-24 - Modals and Global Focus Rings
**Learning:** Modals require `role="dialog"`, `aria-modal="true"`, and appropriate label/description bindings (`aria-labelledby`, `aria-describedby`) for screen readers to recognize them correctly. Additionally, relying on element-specific focus indicators (like `.card:focus-visible`) leaves many interactive elements un-navigable via keyboard.
**Action:** Use `*:focus-visible` to establish a global focus ring baseline instead of piecemeal focus rings, ensuring no interactive element is left behind during keyboard navigation.
