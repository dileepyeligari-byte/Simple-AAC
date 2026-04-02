## 2024-05-24 - Interactive Elements Need Keyboard Support
**Learning:** Custom interactive elements (like the AAC cards rendered as `div`s) must explicitly implement keyboard support (`role="button"`, `tabindex="0"`, and `keydown` event listeners for Enter/Space keys) to be accessible for users who rely on switch controls or keyboard navigation.
**Action:** Always add keyboard accessibility attributes and event listeners when using non-semantic HTML elements for interactivity.
## 2024-05-24 - Action buttons and toast accessibility
**Learning:** Action buttons should visually convey when they are unavailable (disabled state) to prevent confusion. Toast containers must use aria-live regions so screen readers can announce dynamic updates without requiring focus.
**Action:** Add disabled attributes to buttons that require state (e.g., non-empty input/selections), along with visual styles (opacity, cursor). Always add aria-live="polite" to global toast or notification containers.
## 2024-05-24 - Hold-to-Unlock Keyboard Accessibility
**Learning:** Custom "hold-to-unlock" interactions (like the parent gate FAB) often rely on mouse and touch events (`mousedown`/`mouseup`, `touchstart`/`touchend`), which makes them completely inaccessible to keyboard users.
**Action:** When implementing hold-to-unlock UI patterns, explicitly handle keyboard events by adding `keydown` (checking for Enter/Space and ignoring `event.repeat`) and `keyup` handlers to trigger the same gate logic.
