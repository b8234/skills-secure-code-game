# 🛡️ Secure Code Game – Season 2: Level 5

Welcome to **Level 5**, the final challenge of Secure Code Game Season 2! This level is a deep dive into the dark arts of **JavaScript security pitfalls**, focusing on three core vulnerabilities:

- Type Coercion
- Internal Method Exposure
- Prototype Chain Abuse

---

## 🎯 Objective

Harden a SHA-1 implementation (`CryptoAPI.sha1.hash`) against three JavaScript exploits while learning secure programming principles.

You’ll:

- Explore vulnerabilities in `code.js` and `vulnerable_code.js`
- Understand and test exploits using `hack-1.js` through `hack-3.js`
- Implement or analyze the secure solution in `secure_code.js`
- Learn from guided code reviews and hints

---

## 🧪 How to Run

### Option A: Local Browser

1. Open `index.html` in a web browser.
2. Open DevTools → Console.

### Option B: GitHub Codespaces / Terminal

```bash
cd Season-2/Level-5/
python3 -m http.server
````

Open the port 8000 preview in your browser.

---

## 💥 Exploits

Each hack file simulates a real exploit:

| Exploit | File        | Attack Vector                                 | Trigger Example                              |
| ------- | ----------- | --------------------------------------------- | -------------------------------------------- |
| #1      | `hack-1.js` | Type coercion via `toString()`                | `{ toString: () => alert('Exploit 1') }`     |
| #2      | `hack-2.js` | Overwriting internal `_round` function        | `CryptoAPI.sha1._round = () => alert(...)`   |
| #3      | `hack-3.js` | Array prototype abuse with `__defineSetter__` | `Array.prototype.__defineSetter__("0", ...)` |

---

## 🔐 Secure Fixes

Secure defenses implemented in `secure_code.js` and `vulnerable_code.js` include:

| Vulnerability       | Secure Fix                                  |
| ------------------- | ------------------------------------------- |
| Type Coercion       | Validate input with `typeof === "string"`   |
| Method Override     | Store `_round` in a closure-scoped variable |
| Prototype Pollution | Use `Object.create(null)` or prefill arrays |

---

## 🧠 Learning Materials

| File                         | Description                                      |
| ---------------------------- | ------------------------------------------------ |
| `level_5_guide.md`           | Overview of security issues and fixes            |
| `level_5_code_review.md`     | Detailed audit-style code review                 |
| `level_5_lessons_learned.md` | Key takeaways and best practices from this level |

---

## 💡 Hints

If stuck, consult these:

- `hint-1.txt` → Explore coercion via `toString()`
- `hint-2.txt` → Inspect `_round` function scope
- `hint-3.txt` → Analyze how `w` (array) is initialized

---

## 📂 File Structure

```text
.
├── code.js                # Original SHA-1 implementation with flaws
├── vulnerable_code.js     # Version with known vulnerabilities
├── secure_code.js         # Hardened version with all fixes
├── index.html             # Console simulation interface
├── hack-1.js              # Exploit 1 – input coercion
├── hack-2.js              # Exploit 2 – internal method override
├── hack-3.js              # Exploit 3 – prototype setter attack
├── hint-1.txt             # Hint for Exploit 1
├── hint-2.txt             # Hint for Exploit 2
├── hint-3.txt             # Hint for Exploit 3
├── level_5_guide.md       # Overview and learning framework
├── level_5_code_review.md # Audit notes and code critique
└── level_5_lessons_learned.md # Summary of key takeaways
---
```

## ✅ Completion Criteria

To complete this level:

- Trigger each exploit (3 total) using the JavaScript console
- Understand the root causes
- Validate that `secure_code.js` resists all 3 exploits

---

## 🧩 Final Thought

> In JavaScript, **every object is mutable**, even built-ins. The best defense? Anticipate how your code might be twisted—and defend accordingly.

Good luck, and well done for reaching the final level!
