# 🛡️ Secure Code Game – Season 1 / Level 3: Path Traversal Defense

Welcome to Level 3 of the Secure Code Game! This level focuses on defending against **path traversal attacks** — a common vulnerability in file-handling logic.

---

## 🔍 Objective

You are working with a `TaxPayer` class that allows users to upload and retrieve:

- A profile picture (optional)
- A tax form (required)

Your challenge is to **detect and defend** against malicious user-supplied file paths that may try to access sensitive files outside the allowed directory.

---

## 📁 Project Structure

```text
.
├── code.py                # Core implementation (partially secure)
├── hack.py                # Contains simulated path traversal attacks
├── tests.py               # Valid test cases for safe inputs
├── vulnerable_code.py     # Baseline insecure version of the app
├── secure_code.py         # Hardened secure version using allow-list principles
├── solution.py            # Reference solution with proper path validation
├── hint.txt               # Hints about input validation strategy
├── tax_form.pdf           # Sample input for testing tax form attachment
├── path_traversal_guide.md            # Tutorial-style explanation for Level 3
├── path_traversal_lessons_learned.md  # Summary of weaknesses & lessons learned
├── secure_python_code_review.md       # Code review guidance on secure file access
````

---

## 🧠 Key Concepts

### ❌ Path Traversal

Path traversal occurs when user input like `../../etc/passwd` is used to escape the intended directory and read arbitrary files.

### ✅ Secure Strategy

1. **Normalize** file paths with `os.path.normpath` and `os.path.abspath`
2. **Restrict** access to a base directory using `startswith()`
3. **Use an allow-list**, not a block-list
4. **Test both valid and malicious inputs**

---

## 🧪 How to Run the Tests

### Run Valid Behavior Tests

```bash
python tests.py
```

This validates that standard use cases (e.g., accessing `assets/prof_picture.png`) behave correctly and stay within the expected directory.

### Run Hack Simulation

```bash
python hack.py
```

This tests whether malicious inputs (e.g., path traversal attacks) are properly blocked.

---

## 🔐 Secure Version

The `secure_code.py` file contains the most robust version of the `TaxPayer` class. It uses:

- An enforced `SAFE_ROOT` directory (`./assets`)
- A private `_resolve_safe_path()` helper to normalize and validate paths
- Rejection of absolute paths or inputs starting with `..`

---

## 💡 Tips & Best Practices

From `hint.txt` and the included reviews:

- Prefer **allow-lists** of trusted patterns or base directories
- Avoid fragile block-lists like `if '..' in path`
- Always write unit tests for **malicious** and **valid** cases

---

## 📚 Learn More

- [`path_traversal_guide.md`](path_traversal_guide.md): Strategy and concepts explained
- [`path_traversal_lessons_learned.md`](path_traversal_lessons_learned.md): Examples and cheat sheet
- [`secure_python_code_review.md`](secure_python_code_review.md): Secure coding checklist for Python

---

## ✅ Success Criteria

To complete this level:

- Harden the `code.py` implementation (or write your own)
- Block all traversal attempts (`hack.py` returns `None`)
- Pass all valid tests (`tests.py` passes completely)
- Write clear, validated file access logic

Good luck, and remember: **never trust user input paths. Ever.**
