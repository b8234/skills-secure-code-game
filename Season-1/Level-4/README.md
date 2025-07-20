# 🛡️ Level 4 – SQL Injection Defense: Secure Stock Database

This project is part of a secure coding challenge designed to help developers identify and remediate SQL injection vulnerabilities in Python applications.

It demonstrates the evolution from **vulnerable code** to a **secure, testable, and production-ready implementation** using input validation and parameterized queries.

---

## 📁 Project Structure

```bash
.
├── code.py                # Original insecure implementation
├── vulnerable_code.py     # Refactored but still risky version
├── secure_code.py         # Final secure version using parameterization and validation
├── solution.py            # Conceptual explanation of secure and insecure patterns
├── hint.py                # Brief vulnerability hint and example
├── tests.py               # Unit tests for secure_code.py
├── hack.py                # Simulated SQL injection attempts
├── secure_test_runner.py  # Test harness for both secure & compatible modes
├── secure_server.py       # REST API exposing secure database operations
├── sql_injection_guide.md          # Guide on identifying and fixing SQL injection
├── sql_injection_code_review.md   # Best practices and code review heuristics
├── sql_injection_lessons_learned.md # Summary of key takeaways from this level
└── level-4.db             # SQLite database (auto-generated)
````

---

## 🧠 Challenge Goals

1. **Understand how SQL injection works**
2. **Refactor insecure logic to use safe patterns**
3. **Validate user input before executing database operations**
4. **Test both expected and exploit behavior**

---

## ✅ Secure Features Implemented

* 🔐 **Parameterized queries** prevent malicious SQL injection
* ✅ **Stock symbol validation** using `isalnum()`, uppercase enforcement, and length check
* 🔁 **Test-compatible logging** using `secure` and `compatible` modes
* 🔄 **Auto-database initialization** for consistent testing

---

## 🚀 How to Use

### 1. Run the tests to initialize and validate the secure database

```bash
python tests.py
```

### 2. Simulate attacks using

```bash
python hack.py
```

> Note: This may alter the database. To reset it, delete `level-4.db` and re-run `tests.py`.

### 3. Run the secure test harness

```bash
python secure_test_runner.py
```

### 4. Launch the REST API (optional)

```bash
python secure_server.py
```

* GET `/stock-info?symbol=MSFT`
* GET `/stock-price?symbol=MSFT`
* POST `/update-price` with JSON body

---

## 🧪 Test Modes

The secure implementation supports two modes:

* `secure`: strict logging with placeholders (`?`)
* `compatible`: logs expected output format for test harness

Both modes ensure parameter safety — only logging behavior changes.

---

## ⚠️ Vulnerable Patterns to Avoid

| Vulnerability       | Bad Pattern                             | Secure Fix                             |
| ------------------- | --------------------------------------- | -------------------------------------- |
| Raw SQL Strings     | `"SELECT * FROM table WHERE x = '" + x` | `"SELECT * FROM table WHERE x = ?"`    |
| `executescript()`   | Executes arbitrary multi-line SQL       | `execute()` with placeholders          |
| No Input Validation | Any user input allowed                  | `isalnum(), isupper(), len <= 5` check |

---

## 📚 Learn More

* [SQL Injection Guide](sql_injection_guide.md)
* [Code Review Checklist](sql_injection_code_review.md)
* [Lessons Learned](sql_injection_lessons_learned.md)

---

## 🔒 Mantra

> "User input is hostile until proven harmless.
> Parameterize everything. Trust nothing."

---
