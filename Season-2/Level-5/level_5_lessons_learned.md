# 📄 `level_5_lessons_learned.md`

````markdown
# 📄 `level_5_lessons_learned.md`

## Level 5 – Lessons Learned: JavaScript Coercion, Method Exposure, and Prototype Tampering

---

## 1. What Went Wrong

Despite appearing functional and passing basic usage, the SHA-1 hash function had no safeguards against malicious input or prototype misuse.

### Mistakes

```js
// ❌ No input type validation
CryptoAPI.sha1.hash({ toString: () => alert("Exploit!") });

// ❌ Exposed internal method
CryptoAPI.sha1._round = () => alert("Exploit!");

// ❌ Unsafe array structure
Array.prototype.__defineSetter__("0", () => alert("Exploit!"));
````

---

## 2. Exploit Mechanisms

| Vulnerability    | Attack Strategy                                     |
| ---------------- | --------------------------------------------------- |
| Input Coercion   | Object with `toString()` triggers during processing |
| Method Override  | `_round()` replaced with attacker logic             |
| Prototype Setter | Array index setter used for malicious side effects  |

---

## 3. Why Tests Weren’t Enough

Tests assumed:

* Input was always a clean string
* Internal methods weren’t overwritten
* Arrays were safe to use unprotected

🧠 But attackers exploited JS’s dynamic behavior to bypass all assumptions.

---

## 4. Fix Summary

```text
| Problem               | Fix                                                       |
|------------------------|------------------------------------------------------------|
| Unchecked Input        | Add `typeof` check to reject objects                      |
| Internal Exposure      | Use closure for internal function references              |
| Prototype Vulnerability| Use `Object.create(null)` or prefilled arrays             |

---
```

## 5. Takeaways

```text
| Area                 | Secure Practice                                                |
|----------------------|----------------------------------------------------------------|
| Input Validation     | Always check data types before processing                      |
| Internal Encapsulation | Use function scope to prevent method tampering              |
| Structure Safety     | Avoid relying on built-in prototypes (especially in arrays)    |
| JavaScript Mindset   | Assume anything public can be mutated — defend accordingly     |

---
```

## 6. Key Reminder

> “In JavaScript, even arrays and functions are attack surfaces — code defensively.”

---

### Files That Show the Journey

* `code.js` – original insecure implementation
* `vulnerable_code.js` – had unsafe coercion and exposed internals
* `secure_code.js` – mitigates all three attack vectors
* `hack-1.js`, `hack-2.js`, `hack-3.js` – exploit simulations
* `hint-1.txt`, `hint-2.txt`, `hint-3.txt` – guided hint path for exploit discovery
