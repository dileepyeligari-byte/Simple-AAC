## 2024-05-24 - Interactive Elements Need Keyboard Support
**Learning:** Custom interactive elements (like the AAC cards rendered as `div`s) must explicitly implement keyboard support (`role="button"`, `tabindex="0"`, and `keydown` event listeners for Enter/Space keys) to be accessible for users who rely on switch controls or keyboard navigation.
**Action:** Always add keyboard accessibility attributes and event listeners when using non-semantic HTML elements for interactivity.
## 2024-05-25 - Form Controls Need Explicit Labels
**Learning:** Screen readers cannot always infer the purpose of form inputs without proper labeling, leading to a poor experience. Even when visual text is nearby, using `for` attributes on `<label>` elements and `aria-label` when visual labels are omitted is crucial.
**Action:** Always link visual text using `<label for="[id]">`, or provide an `aria-label` to form controls like `<input>` and `<select>`.
