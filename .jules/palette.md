## 2024-05-24 - Interactive Elements Need Keyboard Support
**Learning:** Custom interactive elements (like the AAC cards rendered as `div`s) must explicitly implement keyboard support (`role="button"`, `tabindex="0"`, and `keydown` event listeners for Enter/Space keys) to be accessible for users who rely on switch controls or keyboard navigation.
**Action:** Always add keyboard accessibility attributes and event listeners when using non-semantic HTML elements for interactivity.
## 2024-05-24 - Action buttons and toast accessibility
**Learning:** Action buttons should visually convey when they are unavailable (disabled state) to prevent confusion. Toast containers must use aria-live regions so screen readers can announce dynamic updates without requiring focus.
**Action:** Add disabled attributes to buttons that require state (e.g., non-empty input/selections), along with visual styles (opacity, cursor). Always add aria-live="polite" to global toast or notification containers.
## 2024-05-24 - Modals and Global Focus Rings
**Learning:** Custom UI dialogs (like the ones used for Init, Confirm, and Admin) need semantic ARIA roles (`role="dialog"`, `aria-modal="true"`) to properly trap virtual focus and announce themselves to assistive technologies. Additionally, global focus rings (`*:focus-visible`) provide much better and safer accessibility out of the box than targeting specific classes like `.card:focus-visible`.
**Action:** When working on custom dialogs, always ensure they have dialog roles and description attributes. Default to universal focus indicators unless design specifies otherwise.
