# 📄 `level_4_code_review.md`

## Secure Code Review – Level 4: Escaping & Output Context for XSS Defense

---

## 1. What Is This Code Trying To Do?

This Flask application:

* Accepts a planet name via POST request
* Displays information about the planet using a Jinja2 template
* Provides a Google search snippet using JavaScript and DOM manipulation

---

## 2. What’s the Risk?

```text
| Concern              | Issue                                                                 |
|----------------------|-----------------------------------------------------------------------|
| HTML Injection       | Input is displayed in HTML without escaping                           |
| Unsafe Rendering     | Templating uses `| safe`, disabling autoescaping                      |
| Weak Filtering       | Relies on regex to strip characters, which doesn't stop all XSS cases |
| DOM Injection        | JS reads directly from HTML content inserted by user                  |

---
```

## 3. Line-by-Line Review

### A. Weak Regex Sanitization

```python
# ❌ Not sufficient to sanitize HTML/JS input
sanitized_planet = re.sub(r'[<>{}[\]]', '', planet if planet else '')
```

```python
# ✅ Use context-aware escaping
from markupsafe import escape
safe_planet = escape(planet)
```

---

### B. Unsafe Template Rendering

```html
<!-- ❌ Disables escaping -->
<p>Planet name: <span id="name">{{ planet | safe }}</span></p>
```

```html
<!-- ✅ Secure: use autoescaping -->
<p>Planet name: <span id="name">{{ planet }}</span></p>
```

---

### C. DOM Injection Risk

```html
<!-- ❌ Pulls textContent from user input and injects it via innerHTML -->
<script>
  document.getElementById("planet").innerHTML = document.getElementById("name").textContent;
</script>
```

```html
<!-- ✅ Avoid unnecessary JS reflection or encode properly -->
<script>
  const name = document.getElementById("name").textContent;
  document.getElementById("planet").textContent = name;
</script>
```

---

## 4. Secure Coding Checklist: XSS Defense

* [x] Never use `| safe` with untrusted input
* [x] Escape user input before rendering
* [x] Avoid over-reliance on regex filtering
* [x] Be mindful of DOM injection via JavaScript
* [x] Trust escaping, not sanitizing

---

## 5. Mantra

> “Sanitize on input, escape on output — never blindly trust templates.”

---

## References

* `code.py`, `secure_code.py`
* `details.html`, `index.html`
* `tests.py`, `hack.txt`
