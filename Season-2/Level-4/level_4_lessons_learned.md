# 📄 `level_4_lessons_learned.md`

## Level 4 – Lessons Learned: Escaping, XSS, and Templating Trust

---

## 1. What Went Wrong

The application passed all unit tests — but failed in the face of a **real-world attack vector**.

### Mistakes

```python
# ❌ Regex-based sanitization is fragile
sanitized_planet = re.sub(r'[<>{}[\]]', '', planet)

# ❌ Dangerous rendering shortcut
{{ planet | safe }}
```

---

## 2. Exploit Mechanisms

| Vulnerability    | Attack Strategy                                           |
|------------------|-----------------------------------------------------------|
| HTML Injection   | Insert `<img src=x onerror=alert(1)>` directly in form    |
| Script Execution | Template renders it without escaping                      |
| DOM Injection    | JavaScript reflects unsafe text into the page             |

---

## 3. Why Tests Weren’t Enough

The `tests.py` file focused on:

* Presence of expected text
* Blocking known `script` tags
* Form submission behavior

🧠 But the attacker used an `<img>` tag with `onerror`, which bypassed naive regex filters and wasn’t caught by static tests.

---

## 4. Fix Summary

```text
| Problem             | Fix                                                   |
|---------------------|--------------------------------------------------------|
| Output Escaping     | Use `markupsafe.escape()` before rendering             |
| Template Filtering  | Remove `| safe` to let Jinja2 autoescape               |
| Regex Assumptions   | Don’t assume character filtering can block XSS safely  |
| JS Reflection       | Avoid unnecessary innerHTML injection in client-side JS|

---
```

## 5. Takeaways

```text

| Area             | Secure Practice                                            |
|------------------|------------------------------------------------------------|
| Output Handling  | Escape before rendering to HTML                            |
| Template Logic   | Don’t override built-in escaping with `| safe`             |
| Input Validation | Don’t rely on regex for sanitizing HTML/JS                |
| JavaScript       | Avoid reflecting user-controlled content into the DOM      |
| Mental Model     | Always think: “What if this was untrusted input?”         |

---
```

## 6. Key Reminder

> “Escaping is a context-aware defense — regex is not.”

---

### Files That Show the Journey

* `code.py` – flawed logic with `| safe` and weak filtering  
* `ha*
