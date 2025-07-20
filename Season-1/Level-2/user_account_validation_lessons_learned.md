# Level 2 – User Account Validation: Real Examples & Lessons Learned

---

## 1. Vulnerable Implementation Example (`code.h`)

```c
v = strtol(value, &endptr, 10);
if (*endptr || i >= SETTINGS_COUNT)
    return false;
accounts[user_id]->setting[i] = v;
````

**Why it fails:**

* No lower bound (`i < 0`) check allows negative indices.
* Writing to `setting[-7]` writes to the `isAdmin` flag—enabling privilege escalation.

---

## 2. Secure Implementation Example (Best Practice Fix)

```c
if (i < 0 || i >= SETTINGS_COUNT)
    return false;
accounts[user_id]->setting[i] = v;
```

**Why it works:**

* Both bounds checked; only valid setting indices are accepted.
* Negative indices and overflows are blocked.
* Prevents attackers from writing to unintended struct fields.

---

## 3. Professional-Grade Hardened Fix Example

```c
if (!index || index[0] == '\0' || *endptr != '\0')
    return false;
if (i < 0 || i >= SETTINGS_COUNT)
    return false;
size_t idx = (size_t)i;
accounts[user_id]->setting[idx] = v;
```

**Why it's best practice:**

* Checks for null/empty index, strict string parsing, and safe casting.
* Defends against future struct changes and unexpected input.

---

## 4. Test & Hack Files – Learning Through Examples

* **`tests.c`:** Confirms standard user flows and rejects unauthorized privilege escalation.
* **`hack.c`:** Simulates an attack by attempting a negative index exploit; should be blocked in secure code.

---

## Cheat Sheet: Memory-Safe Coding Lessons

1. **Always check array bounds (both sides!).**
2. **Never trust user input—validate everything.**
3. **Review struct layouts for risky field adjacency.**
4. **Test with both normal and “evil” input.**
5. **Document your checks for future maintainers.**

---
