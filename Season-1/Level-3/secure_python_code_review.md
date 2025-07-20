# Secure Python Code Review – Level 3: Path Traversal Defense

---

## 1. What Is This Code Trying To Do?

We are reviewing a `TaxPayer` class with two key methods:

- `get_prof_picture(path=None)`: Optional. Loads a profile picture.
- `get_tax_form_attachment(path=None)`: Required. Loads a submitted tax form.

Both methods take a user-controlled `path` input and attempt to open a file.

```python
with open(path, 'rb') as form:
    tax_data = bytearray(form.read())
```

> ⚠️ Problem: These methods process **user input directly** as file paths.

---

## 2. Line-by-Line: Trust, Validate, Guard

### `get_prof_picture`

This function has a basic defense:

```python
if path.startswith('/') or path.startswith('..'):
    return None
```

But that's not enough. A better approach uses path normalization:

```python
base_dir = os.path.dirname(os.path.abspath(__file__))
prof_picture_path = os.path.normpath(os.path.join(base_dir, path))
```

Still, **it lacks an allow list or proper boundary check.**

### `get_tax_form_attachment`

This method has **no validation at all**:

```python
with open(path, 'rb') as form:
    tax_data = bytearray(form.read())
```

> ⚠️ A malicious user can supply:
>
> ```python
> input = '/etc/passwd'  # or '../../../../etc/shadow'
> ```
>
> This would read arbitrary system files.

---

## 3. Exploit Thinking: What Could Go Wrong?

In `hack.py`, the attacker simply does:

```python
input = './../../../../../etc/passwd'
output = test_obj.get_tax_form_attachment(input)
```

> If there's no check, the file gets read. Critical breach.

Even if the attacker doesn’t get a response, they may confirm existence or content.

---

## 4. Strong Defensive Fix: Normalize + Contain

### ✅ Good: Base Path Enforcement

```python
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'assets'))
resolved_path = os.path.abspath(os.path.join(base_dir, path))

if not resolved_path.startswith(base_dir):
    return None
```

### ✅ Better: Allow List by Extension

```python
allowed_extensions = ['.png', '.pdf']
if not os.path.splitext(path)[1] in allowed_extensions:
    return None
```

> **Allow lists beat block lists** for user-controlled input.

---

## 5. Final Secure Example (Refactored)

```python
def get_safe_file(base_subdir, path):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), base_subdir))
    resolved_path = os.path.abspath(os.path.join(base_dir, path))

    if not resolved_path.startswith(base_dir):
        raise Exception("Invalid file path")

    with open(resolved_path, 'rb') as f:
        return bytearray(f.read())

def get_prof_picture(self, path=None):
    if not path:
        return None
    return get_safe_file('assets', path)

def get_tax_form_attachment(self, path=None):
    if not path:
        raise Exception("Tax form is required")
    return get_safe_file('assets', path)
```

---

## 6. Train Your Brain: Path Traversal Checklist 🏋️

- ✅ Is the path **normalized** using `os.path.abspath()` and `os.path.normpath()`?
- ✅ Is user input **restricted to a known base directory**?
- ✅ Is an **allow list** used for file extensions?
- ❌ Are we relying only on block lists like `if '..' in path`? (**Not enough!**)
- ✅ Do tests exist for both valid and malicious paths?

---

## 🧠 Secure Coding Mantra (Path Edition)

> "User paths are not gifts. They’re traps. Contain them, resolve them, and never trust them."

---

## References

- `code.py` and `hack.py` for real-world examples.
- `tests.py` for test validation with trusted directories.
- `hint.txt`: Allow list > Block list.
