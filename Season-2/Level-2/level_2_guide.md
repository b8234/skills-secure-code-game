# 📄 `level_2_guide.md`

````markdown
# Level 2 – Secure Login Practices: Preventing Enumeration & Sensitive Logging

---

## 1. Understanding the Problem

### Context

This level simulates a common web authentication scenario. A `loginHandler` accepts an email and password via POST request and authenticates against mock users.

### Issue

Although the tests pass initially, the code introduces dangerous security flaws:

| Component            | Flaw                                                   |
|---------------------|--------------------------------------------------------|
| Login Feedback       | Reveals whether email exists (user enumeration risk)  |
| Logging              | Logs email and password (sensitive data exposure)     |
| Error Messaging      | Returns different messages for known/unknown users    |

---

## 2. Key Concepts: Secure Login Design

### A. User Enumeration

❌ Insecure

```go
if !ok {
  http.Error(w, "invalid email or password", http.StatusUnauthorized)
}
````

✅ Secure

```go
// Generic response for both wrong email or password
http.Error(w, "Invalid Email or Password", http.StatusUnauthorized)
```

---

## B. Sensitive Log Statements

❌ Insecure

```go
log.Printf("User %q logged in successfully with a valid password %q", email, password)
```

✅ Secure

```go
log.Printf("Successful login request")
```

---

### C. Input Validation

```go
if !isValidEmail(email) {
  http.Error(w, "Invalid email format", http.StatusBadRequest)
}
```

🧠 Note: Validating input format early avoids deeper processing of malformed data.

---

## 3. Fixing the Vulnerable Code

| Vulnerability          | Secure Fix                                     |
| ---------------------- | ---------------------------------------------- |
| Enumeration            | Unified error message for auth failure         |
| Email/Password Logging | Remove sensitive values from logs              |
| Input Validation       | Maintain minimal logs with no user-identifiers |

---

## 4. Test Coverage

### `code_test.go`

Covers valid/invalid credentials, malformed emails, wrong HTTP method, and unknown fields.

### `hack_test.go`

* Detects **user enumeration**
* Flags **sensitive log output**

---

## 5. Training Your Brain

| Area            | Ask Yourself                                     |
| --------------- | ------------------------------------------------ |
| Logging         | Is any user info (email/password) being logged?  |
| Error Messaging | Are error messages giving attackers information? |
| Test Thinking   | Do logs leak data even when the UI looks fine?   |

---

## Referenced Files

* `code.go` – vulnerable implementation
* `code_test.go` – tests pass but don’t detect flaws
* `hack_test.go` – tests that expose vulnerabilities
* `solution.go` – fixed version
* `solution_test.go` – validates secure behavior
