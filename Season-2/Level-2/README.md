# 🛡️ Secure Code Game – Season 2 / Level 2

Welcome to **Level 2** of the Secure Code Game! This level challenges you to detect and patch serious vulnerabilities in a basic authentication server.

---

## 🎯 Objective

**Fix the security flaws in `code.go` so that:**

1. ✅ `code_test.go` still passes
2. ✅ `hack_test.go` passes (no more exploits!)
3. ✅ You understand how to avoid:
   - User enumeration
   - Sensitive data logging

---

## 🔍 Vulnerabilities to Fix

| 🔓 Flaw                    | 🚨 Issue Description                                        |
|---------------------------|-------------------------------------------------------------|
| User Enumeration          | Different responses for invalid email vs. wrong password    |
| Logging Sensitive Data    | Logs reveal email addresses and passwords                   |
| Detailed Error Messages   | HTTP responses expose too much info to potential attackers  |

---

## 📂 File Structure

| File                         | Description |
|------------------------------|-------------|
| `code.go`                    | 🧪 Vulnerable implementation of the login handler |
| `code_test.go`               | ✅ Functional tests – all passing by default |
| `hack_test.go`               | 🚨 Tests that reveal security flaws in `code.go` |
| `solution/solution.go`       | ✅ Fully secured and patched implementation |
| `solution/solution_test.go`  | 🔐 Combined test suite that validates secure behavior |
| `hint-1.txt`                 | 🧠 Hint: Think about how attackers enumerate users |
| `hint-2.txt`                 | 🧠 Hint: Look closely at what is logged |
| `level_2_guide.md`           | 📘 Walkthrough of the vulnerabilities and concepts |
| `level_2_code_review.md`     | 🔍 Annotated code review with secure vs insecure examples |
| `level_2_lessons_learned.md` | 🧾 Summary of what you should learn from this level |

---

## 🧪 How to Run

Make sure you have Go installed: [https://go.dev/dl](https://go.dev/dl)

### 1. Run the vulnerable tests

```bash
go test -v code.go code_test.go
````

### 2. Run the hack tests (they should FAIL at first)

```bash
go test -v code.go hack_test.go
```

### 3. Fix `code.go` and verify all tests now pass ✅

### 4. (Optional) Compare your solution

```bash
go test -v solution/solution.go solution/solution_test.go
```

---

## 🧠 Key Concepts to Apply

- 🕵️ Use **generic login error messages**
- 🚫 **Never log** sensitive data (like emails or passwords)
- ✅ Perform **input validation** before logging
- 🔍 Use **hack-style tests** to catch what functional tests miss

---

## ✅ Victory Conditions

- [ ] All tests in `code_test.go` and `hack_test.go` pass
- [ ] You understand why those changes make the app more secure
- [ ] You can spot and fix similar issues in future code

---

## 💬 Mantra

> “If an attacker can tell if a user exists, they will. Hide everything.”

Good luck!
