# 📄 `level_2_code_review.md`

````markdown
# Secure Code Review – Level 2: Preventing User Enumeration & Sensitive Logging

---

## 1. What Is This Code Trying To Do?

This Go server implements a `/login` endpoint that:

* Accepts email and password
* Checks credentials against mock data
* Returns status codes based on validity

---

## 2. What’s the Risk?

| Concern                      | Issue                                                     |
|-----------------------------|------------------------------------------------------------|
| User Enumeration             | Different messages for invalid email vs. password         |
| Logging Sensitive Data       | Emails and passwords printed in logs                      |
| Inconsistent HTTP Responses  | Reveals too much through HTTP status + body               |

---

## 3. Line-by-Line Review

### A. Logging User Credentials

```go
// ❌ Leaks user information
log.Printf("User %q logged in successfully with a valid password %q", email, password)
````

```go
// ✅ Secure version
log.Printf("Successful login request")
```

---

## B. Revealing Login Status

```go
// ❌ Reveals user existence
http.Error(w, "invalid email or password", http.StatusUnauthorized)
```

```go
// ✅ Secure version
http.Error(w, "Invalid Email or Password", http.StatusUnauthorized)
```

---

### C. Logging Invalid Emails

```go
// ❌ Logs invalid email format (still leaks input)
log.Printf("Invalid email format: %q", email)
```

```go
// ✅ Secure version
log.Printf("Invalid email format")
```

---

## 4. Secure Coding Checklist: Login Edition

* [x] Use generic error messages
* [x] Never log email or password inputs
* [x] Use proper status codes (`401`, `400`, etc.)
* [x] Validate input before processing
* [x] Avoid logging user-identifiable data

---

## 5. Mantra

> “If an attacker can tell if a user exists, they will. Hide everything.”

---

## References

* `code.go`, `code_test.go`
* `hack_test.go`, `solution.go`, `solution_test.go`
