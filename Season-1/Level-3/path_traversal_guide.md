# Level 3 – Path Traversal Defense: Input Sanitization & Directory Control

---

## 1. Understanding the Problem

**Context:**

* A `TaxPayer` class provides methods to retrieve a user’s profile picture and tax form.
* Both methods rely on file paths supplied by users.

**Goal:**
Prevent **path traversal attacks** that could let attackers read arbitrary files by manipulating the file path input.

---

## 2. Breaking Down the Solution(s)

### Key Concepts

* **Path Traversal:**
  Attackers use `../` sequences to escape the intended directory and access unauthorized files (e.g., `/etc/passwd`).

* **Input Validation Techniques:**

  * Reject or sanitize paths containing `..`, `/`, or absolute path indicators.
  * Use `os.path.normpath()` + base directory to anchor access within an allowed folder.

* **Whitelist vs. Blacklist:**

  * Avoid relying on blacklist logic (e.g., checking for `".."`).
  * Instead, **allow only safe, explicitly trusted paths** within a known directory (whitelisting).

---

## 3. How the "Hack" Works and How the Solution Blocks It

**From `hack.py`:**

```python
input = './../../../../../etc/passwd'
output = test_obj.get_prof_picture(input)
```

* This input exploits directory traversal to try accessing system files.
* The secure logic in `get_prof_picture()` returns `None` if path starts with `/` or `..`.

**From `code.py`:**

```python
if path.startswith('/') or path.startswith('..'):
    return None
```

* This blocks path traversal *before* trying to resolve or read the file.
* Further protection: `os.path.normpath` and joining with the base directory ensures controlled file access.

---

## 4. Test-Driven Mindset

### Standard Tests – `tests.py`

* Confirm that normal profile and tax form access works as expected.
* Assert that the **resulting path** remains within the base directory.

### Hack Tests – `hack.py`

* Use malicious inputs like `../../../../../etc/passwd`.
* Assert that these inputs return `None` and do not escape the base directory.

---

## 5. How to Train Yourself for These Challenges

* **Question all user input** that influences file paths.
* **Normalize and resolve** paths *after* joining with a known base directory.
* **Never trust file paths** given by users—even ones that look benign.
* Test against all suspicious patterns: `..`, `/`, `\`, `%2e`, etc.

---

## Summary Table: What to Focus On

| Area             | Questions to Ask / What to Look For                    |
| ---------------- | ------------------------------------------------------ |
| Input Validation | Does the path start with `/` or `..`?                  |
| Path Resolution  | Is the final resolved path still within allowed scope? |
| Abuse Cases      | Can user inputs access unauthorized files?             |
| Defensive Coding | Are all file accesses restricted to safe directories?  |
| Testing          | Are malicious path traversal cases blocked completely? |

---

## 📁 Referenced Files in This Level

* [`code.py`](code.py): Main logic for `TaxPayer` class.
* [`hack.py`](hack.py): Simulates malicious input attacks.
* [`tests.py`](tests.py): Validates standard and secure behavior.
* [`hint.txt`](hint.txt): Suggests using allow-lists over block-lists.
* [`tax_form.pdf`](tax_form.pdf): Sample input file to test safe tax form access.

---

Would you like me to save this as `level_3_path_traversal_defense.md`?
