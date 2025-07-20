# 🛡️ Secure Code Game – Level 4: Cross-Site Scripting (XSS) Defense

Welcome to Level 4 of the Secure Code Game – a hands-on challenge to identify, exploit, and patch a real-world **XSS vulnerability** in a Flask web app.

---

## 🚀 Objective

Fix the vulnerability in `code.py` so that:

- Malicious input (like `<img src=x onerror=alert(1)>`) **does not trigger a script**.
- All tests in `tests.py` pass.
- Input is safely rendered in HTML templates and the DOM.

---

## 🧩 File Overview

```text

| File                        | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| `code.py`                   | Vulnerable version of the app. Uses regex for input sanitization and unsafe `| safe` rendering. |
| `secure_code.py`            | ✅ Final secure solution. Uses `markupsafe.escape()` and removes unsafe rendering practices. |
| `vulnerable_code.py`        | Another flawed version that attempts filtering but still allows unsafe output. |
| `tests.py`                  | Unit tests validating normal behavior, edge cases, and basic attack prevention. |
| `hack.txt`                  | Simulated attack script using an `<img onerror>` XSS vector to test input handling. |
| `index.html`                | Front-end form to submit planet names. Sends POST request to Flask app. |
| `details.html`              | Displays the planet name and description. Initially rendered using `| safe`. |
| `package.json`              | Contains configuration for JS testing libraries (`mocha`, `vitest`). Not required for Python code but may be used for client-side testing. |
| `level_4_guide.md`          | Detailed breakdown of the XSS vulnerability, how to fix it, and how autoescaping works. |
| `level_4_code_review.md`    | Secure code audit covering line-by-line issues in rendering, filtering, and DOM usage. |
| `level_4_lessons_learned.md`| Postmortem summary of what went wrong, what was fixed, and how to avoid similar pitfalls. |

---
```

## 🧪 How to Run

### 1. Install Python dependencies

```bash
pip install flask flask-testing markupsafe
````

### 2. Run the vulnerable version (to observe the issue)

```bash
export FLASK_APP=code.py
flask run
```

### 3. Run the secure version (after applying fix)

```bash
export FLASK_APP=secure_code.py
flask run
```

### 4. Run tests

```bash
python3 tests.py
```

### 5. Try the simulated attack

Open the form at `/`, input:

```html
<img src='x' onerror='alert(1)'>
```

✔️ In the secure version, this should **not** trigger a browser alert.

---

## ✅ Security Fix Summary

| Area               | Secure Practice                                                   |                                        |
| ------------------ | ----------------------------------------------------------------- | -------------------------------------- |
| Input Escaping     | Use `markupsafe.escape()` instead of regex for HTML input         |                                        |
| Template Rendering | Avoid \`                                                          | safe\` to preserve Jinja2 autoescaping |
| JavaScript Safety  | Use `.textContent` instead of `.innerHTML` to avoid DOM injection |                                        |

---

## 🧠 What You’ll Learn

- How simple input like `<img>` can become an XSS attack vector
- Why regex sanitization is insufficient for HTML/JS contexts
- The importance of output escaping and secure template logic
- How to test for real-world security vulnerabilities beyond unit tests

---

## 📁 Directory Structure

```text
Level-4/
├── code.py                  # Vulnerable app
├── secure_code.py           # Secure solution
├── vulnerable_code.py       # Insecure alternative for comparison
├── tests.py                 # Unit tests
├── hack.txt                 # Simulated XSS payload
├── templates/
│   ├── index.html           # Input form UI
│   └── details.html         # Output display template
├── package.json             # (Optional) JS test config
├── level_4_guide.md         # Strategy and core explanation
├── level_4_code_review.md   # Code audit with secure checklist
└── level_4_lessons_learned.md # Takeaways and fix breakdown
```

---

## 🔐 Mantra

> "Escape on output, not sanitize on input."

Always let your templating engine handle escaping — not your regex patterns.
