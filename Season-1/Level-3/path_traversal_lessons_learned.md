
# Level 3 – Path Traversal Defense: Real Examples & Lessons Learned

---

## 1. Vulnerable Implementation (`vulnerable_code.py`)

```python
def get_tax_form_attachment(self, path=None):
    if not path:
        raise Exception("Tax form required")
    with open(path, 'rb') as form:
        tax_data = bytearray(form.read())
    return path
```

**Why it fails:**

- Accepts user-controlled `path` with no validation or sanitization.
- Allows attackers to exploit path traversal (e.g., `../../../../etc/passwd`).
- No confinement to a trusted directory.

---

## 2. Mixed Implementation (`code.py`)

### ✅ `get_prof_picture` (Partially Secure)

```python
if path.startswith('/') or path.startswith('..'):
    return None
```

**Why it improves things:**

- Blocks obvious absolute and relative traversals.
- Uses `os.path.normpath()` and `os.path.join()` for safe path construction.

**But it’s not enough:**

- Block lists can be bypassed (`....//....//etc/passwd`, etc.).
- Does not verify that the resolved path stays within the base directory.

---

### ❌ `get_tax_form_attachment` (Still Vulnerable)

```python
with open(path, 'rb') as form:
    tax_data = bytearray(form.read())
```

**Why it’s still unsafe:**

- Reuses the vulnerable logic from `vulnerable_code.py`.
- Provides no protection against malicious paths.

---

## 3. Hardened Implementation (`secure_code.py`)

```python
def get_tax_form_attachment(self, path=None):
    if not path:
        raise Exception("Tax form required")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.normpath(os.path.join(base_dir, path))

    if not full_path.startswith(base_dir):
        raise Exception("Invalid path")

    with open(full_path, 'rb') as form:
        tax_data = bytearray(form.read())
    return full_path
```

**Why it’s best practice:**

- Builds a full normalized path from a fixed base.
- Verifies that the final path starts with the base directory.
- Prevents traversal attacks, even if attackers obfuscate input.

---

## 4. Test & Hack Files – Learning Through Examples

- **`hack.py`:** Uses malicious paths (`../../etc/passwd`) to simulate attacks.
- **`tests.py`:** Verifies valid input stays within bounds and checks if defenses hold.

---

## Cheat Sheet: Path Traversal Defense Lessons

1. **Always resolve user paths with `os.path.abspath()` + `os.path.normpath()`.**
2. **Use allow-lists (trusted base paths), not block-lists (e.g., just checking for `..`).**
3. **Ensure final resolved paths are *within* allowed directory trees.**
4. **Test both expected and malicious inputs (null bytes, encoded traversal, etc.).**
5. **Design for maintainability — attackers evolve, your checks must stay future-proof.**

---
