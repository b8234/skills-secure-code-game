# 📄 `level_5_lessons_learned.md` – Level 5: Lessons Learned – Cryptographic Pitfalls

````markdown
# Level 5 – Cryptography & Randomness: Lessons Learned

---

## 1. What Went Wrong in the Original Code

### The Problem

The original implementation in `code.py` tried to provide cryptographic functionality such as:

- Token generation
- Salt creation
- Password hashing
- Secret key management

But it made critical security mistakes:

```python
# Token generation
''.join(random.choice(alphabet) for _ in range(length))

# Salt generation
salt = ''.join(str(random.randint(0, 9)) for _ in range(21)) + '.'

# Hashing
hashlib.md5(password.encode()).hexdigest()

# Secrets
SECRET_KEY = 'TjWnZr4u7x!A%D*G-KaPdSgVkXp2s5v8'
````

---

## 2. Dangerous Design Patterns

| Design Pattern             | Problem                                           |
| -------------------------- | ------------------------------------------------- |
| `random.choice` for tokens | Not cryptographically secure                      |
| Manual salt generation     | Predictable and low entropy                       |
| MD5 for password hashing   | Fast, weak, and vulnerable to brute-force attacks |
| Hardcoded secrets          | Can be leaked or reused across environments       |
| Mixing SHA256 with bcrypt  | Not recommended without a clear reason            |

---

## 3. How the Exploit Works (via Audit)

This level isn’t about an interactive attack like SQL injection — it’s about **auditing logic**.

### Static Analysis Findings (`hack.py`)

Tools like **CodeQL** highlight:

* Use of `random` for security purposes
* Use of broken algorithms like `MD5`
* Hardcoded secrets in version-controlled files

But tools can only help so much — they won’t stop you from using bad crypto choices.

> 💡 *This level teaches that even if code “works,” it can still be insecure.*

---

## 4. How the Secure Fix Solves It

### Secure Implementation (`secure_code.py`)

| Issue                 | Secure Fix                      |
| --------------------- | ------------------------------- |
| Weak token generation | Uses `secrets.token_urlsafe()`  |
| Manual salt           | Uses `bcrypt.gensalt()`         |
| MD5 hashing           | Uses `bcrypt.hashpw()`          |
| Hardcoded secret      | Loads from `os.environ.get()`   |
| Type checking         | Ensures input is a valid string |

### Improved Test Coverage (`secure_tests.py`)

Tests verify:

* Tokens are unique and long enough
* Hashes are returned as strings
* Verification logic fails on incorrect input or bad types

---

## 5. Takeaways

| Vulnerability Area    | Mistake Made           | Secure Alternative             |
| --------------------- | ---------------------- | ------------------------------ |
| Token Generation      | Used `random`          | Use `secrets`                  |
| Salt Generation       | Manual construction    | Use `bcrypt.gensalt()`         |
| Hashing Algorithm     | Used `MD5`             | Use `bcrypt` or `argon2`       |
| Secret Handling       | Hardcoded in source    | Use environment variables      |
| Password Verification | Lacked type validation | Explicit type and error checks |

---

## 6. Key Reminders

* Never use general-purpose randomness for cryptography.
* Avoid MD5, SHA1, and other fast hashes for passwords.
* Use vetted libraries like `bcrypt`, `argon2`, or `pbkdf2`.
* Load secrets from secure locations — never hardcode them.
* Test for both success and failure scenarios in cryptographic code.

---

### Files That Show the Journey

* `code.py` / `vulnerable_code.py`: Insecure implementation
* `hack.py`: Reminds us automated tools aren’t enough
* `solution.py`: Explanation with secure patterns
* `secure_code.py`: Production-safe implementation
* `tests.py` / `secure_tests.py`: Validate secure behavior
