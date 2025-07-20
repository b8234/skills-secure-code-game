# 🔐 Secure Code Game – Level 5: Cryptography & Secure Randomness

Welcome to **Level 5** of the Secure Code Game – the final and most advanced challenge of Season 1. This level dives into the world of **cryptographic safety**, **randomness**, and **secret management**, testing your ability to recognize and remediate insecure code patterns.

---

## 🧠 Goal of the Challenge

The provided `code.py` offers core cryptographic utilities:

- Token generation
- Password hashing (via SHA256 or MD5)
- Salt construction
- Management of sensitive keys like `SECRET_KEY`

However, the implementation contains critical security flaws.

---

## ❗ Core Vulnerabilities

| Concern                 | Description                                                      |
|-------------------------|------------------------------------------------------------------|
| 🔓 Weak Randomness      | Uses `random.choice()` for tokens — not cryptographically secure |
| 🧂 Predictable Salt      | Manual construction using `random.randint()`                    |
| ☠️ Insecure Hashing      | Uses deprecated `MD5` for password hashing                       |
| 🔐 Hardcoded Secrets     | Secret keys committed in source code                            |
| ⚠️ Pre-Hashing Passwords | Hashes password with SHA256 before bcrypt                       |

---

## 📁 Project Files

| File Name              | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| `code.py`              | Starting code with security issues (original flawed implementation)     |
| `vulnerable_code.py`   | Explicit version of vulnerable implementation, used in early tests      |
| `secure_code.py`       | Production-ready secure version with correct crypto practices           |
| `solution.py`          | Learning-focused secure solution with commentary and correct patterns   |
| `tests.py`             | Unit tests to validate insecure code behavior                          |
| `secure_tests.py`      | Strong test suite validating secure functionality and edge cases        |
| `hack.py`              | Static analysis prompt for CodeQL; teaches that tools alone aren’t enough |
| `hint.txt`             | Design-level hint nudging users toward cryptographic best practices     |
| `level_5_guide.md`     | Walkthrough of core cryptographic concepts and secure fixes             |
| `level_5_code_review.md`| Detailed review of code flaws and remediations                         |
| `level_5_lessons_learned.md`| Summary of mistakes and best practices for future projects        |

---

## ✅ Secure Design Principles Used

- 🔐 `secrets` module for cryptographic randomness
- ✅ `bcrypt.gensalt()` instead of manual salt
- 🚫 Removed use of `MD5`; used `bcrypt` for password hashing
- 🧪 Full test coverage for correct and incorrect input handling
- 🔑 Secrets retrieved from environment variables (`os.environ.get()`)

---

## 🧪 How to Run

### 1. Run Tests

```bash
python3 tests.py           # Run insecure implementation tests
python3 secure_tests.py    # Run tests on secure implementation
````

### 2. Analyze Vulnerabilities

```bash
python3 hack.py            # Static analysis awareness using CodeQL
```

---

## 📌 Lessons From This Level

> Even if code "works," it can still be **insecure**.
> Security demands deliberate choices: vetted libraries, safe defaults, and strict input validation.

---

## 📜 References

- [Python secrets module](https://docs.python.org/3/library/secrets.html)
- [bcrypt documentation](https://pypi.org/project/bcrypt/)
- [CodeQL](https://codeql.github.com/)
- [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)

---

### 🧘 Security Mantra

> “Random ≠ Secure. Don’t roll your own crypto. Trust vetted libraries.”

---
