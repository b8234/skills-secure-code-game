# 📄 `level_2_lessons_learned.md`

````markdown
# Level 2 – Lessons Learned: Authentication & Logging

---

## 1. What Went Wrong

The initial code:

* Passed normal tests
* Failed when audited for **information leaks**

### Mistakes

```go
log.Printf("User %q logged in successfully with a valid password %q", email, password)
http.Error(w, "invalid email or password", http.StatusUnauthorized)
log.Printf("Invalid email format: %q", email)
````

---

## 2. Exploit Mechanisms

| Vulnerability    | Attack Strategy                            |
| ---------------- | ------------------------------------------ |
| User Enumeration | Compare responses for real vs. fake emails |
| Log Injection    | Read logs to extract credentials           |

---

## 3. Why Tests Matter

The default `code_test.go` passed.

The real red flags were found via:

* `hack_test.go` – logs, message content
* `solution_test.go` – ensures secure behavior stays intact

---

## 4. Fix Summary

| Problem          | Fix                                   |
| ---------------- | ------------------------------------- |
| Leaking Logs     | Remove all sensitive info from logs   |
| Enumeration Risk | Always return generic login error     |
| Poor Log Format  | Avoid referencing user inputs in logs |

---

## 5. Takeaways

| Area             | Secure Practice                           |
| ---------------- | ----------------------------------------- |
| Logging          | Never log credentials or user identifiers |
| Error Messaging  | Don’t reveal if user exists               |
| Input Validation | Validate early, fail securely             |
| Testing          | Audit both success and failure paths      |

---

## 6. Key Reminder

> “Security isn’t just about functionality — it’s about what the attacker sees.”

---

### Files That Show the Journey

* `code.go` – flawed
* `hack_test.go` – exploit checker
* `solution.go` – secure fix
* `solution_test.go` – validation
