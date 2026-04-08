## 2024-05-24 - Interactive Elements Need Keyboard Support
**Learning:** Custom interactive elements (like the AAC cards rendered as `div`s) must explicitly implement keyboard support (`role="button"`, `tabindex="0"`, and `keydown` event listeners for Enter/Space keys) to be accessible for users who rely on switch controls or keyboard navigation.
**Action:** Always add keyboard accessibility attributes and event listeners when using non-semantic HTML elements for interactivity.
## 2024-05-24 - Action buttons and toast accessibility
**Learning:** Action buttons should visually convey when they are unavailable (disabled state) to prevent confusion. Toast containers must use aria-live regions so screen readers can announce dynamic updates without requiring focus.
**Action:** Add disabled attributes to buttons that require state (e.g., non-empty input/selections), along with visual styles (opacity, cursor). Always add aria-live="polite" to global toast or notification containers.
## 2024-05-24 - Global Focus Indicator Standardization
**Learning:** In custom design systems like this one, applying `:focus-visible` styles per-element (e.g., `.card:focus-visible`) often leads to inconsistent keyboard navigation experiences, as other interactive elements (buttons, filters) may lack clear focus indicators. Standardizing with `*:focus-visible` ensures global keyboard accessibility.
**Action:** When working on keyboard accessibility in a custom CSS project, replace specific element focus rules with a global `*:focus-visible` selector to guarantee all focusable elements have a consistent visual indicator without bloating individual component styles.
