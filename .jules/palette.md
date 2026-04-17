## 2024-05-24 - Interactive Elements Need Keyboard Support
**Learning:** Custom interactive elements (like the AAC cards rendered as `div`s) must explicitly implement keyboard support (`role="button"`, `tabindex="0"`, and `keydown` event listeners for Enter/Space keys) to be accessible for users who rely on switch controls or keyboard navigation.
**Action:** Always add keyboard accessibility attributes and event listeners when using non-semantic HTML elements for interactivity.
## 2024-05-24 - Action buttons and toast accessibility
**Learning:** Action buttons should visually convey when they are unavailable (disabled state) to prevent confusion. Toast containers must use aria-live regions so screen readers can announce dynamic updates without requiring focus.
**Action:** Add disabled attributes to buttons that require state (e.g., non-empty input/selections), along with visual styles (opacity, cursor). Always add aria-live="polite" to global toast or notification containers.
## 2024-05-24 - Avoid border-radius inheritance on global focus
**Learning:** When implementing global `:focus-visible` styles (e.g., `*:focus-visible`), using `border-radius: inherit;` is dangerous. It forces the focused element to adopt its parent's border-radius, overriding its own intrinsic shape.
**Action:** Let the browser handle the curve of the outline automatically, or apply specific border-radii only where absolutely necessary. Do not use `border-radius: inherit;` on a universal selector.
