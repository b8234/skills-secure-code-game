# 🔐 Secure Code Game – Season 1: Level 2  

## 🧠 Challenge Theme: Memory Safety & Privilege Escalation

---

## 📜 Overview

This level is designed to teach memory safety and defensive programming through hands-on exploitation and mitigation of a classic C vulnerability: out-of-bounds array access leading to **privilege escalation**.

Your mission is to:

1. Identify the bug in `code.h`.
2. Run `tests.c` and understand expected behavior.
3. Run `hack.c` and exploit the vulnerability.
4. Fix the bug using defensive techniques.
5. Validate your fix against the tests and compare with `solution.c`.

---

## 📁 File Descriptions

| File                        | Description |
|----------------------------|-------------|
| `code.h`                   | 💣 Vulnerable header containing all logic: user struct, account creation, and settings update. The main vulnerability lies here. |
| `tests.c`                  | ✅ Passing tests that confirm basic functionality (creating user, updating settings, checking admin status). |
| `hack.c`                   | ❌ Failing test simulating an attack where a non-admin user becomes admin via a negative index exploit. |
| `solution.c`               | ✅ Secure version of `code.h` with comments explaining both the vulnerability and the fix. |
| `vulnerable_code.h`        | 🪲 Slightly different copy of the vulnerable code for comparison and testing fixes. |
| `secure_code.h`            | 🛡️ Hardened version that includes robust input validation, memory-safe indexing, and defensive coding best practices. |
| `hint-1.txt`               | 🔎 Prompt hint to consider how structure layout can be exploited. |
| `hint-2.txt`               | 💡 Directs you to inspect input to understand how `-7` exploits memory layout. |
| `secure_c_code_review.md` | 🧠 Brain-training guide with step-by-step strategy for reviewing C code for memory issues. |
| `secure_user_account_validation_guide.md` | 📘 Memory safety and privilege escalation prevention checklist for updating user accounts. |
| `user_account_validation_lessons_learned.md` | 🧾 Case study highlighting bad vs. good vs. best practice with real code snippets. |

---

## ⚠️ Core Vulnerability (in `code.h`)

```c
if (*endptr || i >= SETTINGS_COUNT)
    return false;
accounts[user_id]->setting[i] = v;
````

### ❌ What's wrong?

* No check for `i < 0`
* Allows writing before the start of the `setting[]` array
* Adjacent field `isAdmin` is overwritten, allowing a privilege escalation

---

## ✅ Secure Fix Example

```c
if (i < 0 || i >= SETTINGS_COUNT)
    return false;
```

### 🧠 Hardened Fix

```c
if (!index || index[0] == '\0' || *endptr != '\0')
    return false;
if (i < 0 || i >= SETTINGS_COUNT)
    return false;
size_t idx = (size_t)i;
accounts[user_id]->setting[idx] = v;
```

---

## 🧪 How to Run the Code

### Run the standard tests

```bash
make -B Season-1/Level-2/tests && ./Season-1/Level-2/tests
```

### Run the hack attempt

```bash
make -B Season-1/Level-2/hack && ./Season-1/Level-2/hack
```

### Validate your secure implementation

* Replace `code.h` with `secure_code.h` (or use `solution.c` as a guide)
* Rerun both `tests.c` and `hack.c` – both should pass

---

## 🎯 Learning Objectives

* Understand how memory layout affects security
* Prevent privilege escalation via array bounds checks
* Practice defensive programming in C
* Think like an attacker and a secure coder

---

## 🧠 Bonus: Train Your Brain

Use the markdown guides provided to improve your secure coding mindset:

* `secure_c_code_review.md`
* `secure_user_account_validation_guide.md`
* `user_account_validation_lessons_learned.md`

---

## 👨‍💻 Contributing

Want to add your own levels or improve this one?
See [Contributing Guidelines](https://github.com/skills/secure-code-game/blob/main/CONTRIBUTING.md)

---

## 🚀 Good luck & code defensively
