with open('index.html', 'r') as f:
    content = f.read()

content = content.replace(
    '<div id="init-modal" class="modal-overlay">\n    <div class="modal-card">\n        <h2 style="margin-top:0;">Welcome! 👋</h2>',
    '<div id="init-modal" class="modal-overlay" role="dialog" aria-modal="true" aria-labelledby="init-title">\n    <div class="modal-card">\n        <h2 id="init-title" style="margin-top:0;">Welcome! 👋</h2>'
)

content = content.replace(
    '<div id="confirm-modal" class="modal-overlay">\n    <div class="modal-card" style="text-align:center;">',
    '<div id="confirm-modal" class="modal-overlay" role="dialog" aria-modal="true" aria-labelledby="confirm-title" aria-describedby="confirm-body">\n    <div class="modal-card" style="text-align:center;">'
)

content = content.replace(
    '<div id="admin-modal">\n    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:24px;">\n        <h2 id="admin-title">Add/Edit Card</h2>',
    '<div id="admin-modal" role="dialog" aria-modal="true" aria-labelledby="admin-title">\n    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:24px;">\n        <h2 id="admin-title">Add/Edit Card</h2>'
)

content = content.replace(
    '.card:focus-visible { outline: 3px solid var(--primary); outline-offset: 2px; }',
    '*:focus-visible { outline: 3px solid var(--primary); outline-offset: 2px; }'
)

with open('index.html', 'w') as f:
    f.write(content)
