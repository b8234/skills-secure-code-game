# 📄 `level_5_guide.md` – Level 5: Cryptography & Secure Randomness

````markdown
# Level 5 – Cryptography & Secure Randomness: Proper Hashing and Token Generation

---

## 1. Understanding the Problem

### Context

The original `code.py` implements functions to:

- Generate tokens (e.g., API keys, password reset links)
- Create password hashes (with `SHA-256` or `MD5`)
- Manage sensitive constants like `SECRET_KEY`

### Issue

While the intent is good, the implementation has serious flaws:

| Component       | Flaw                                                           |
|----------------|----------------------------------------------------------------|
| Token generation | Uses `random.choice` — not cryptographically secure           |
| Salt generation  | Manually constructs salt using low-entropy digits             |
| Password hashing | Uses `MD5` — outdated and broken                              |
| Secret handling  | Hardcodes secrets into source code                            |

---

## 2. Key Concepts: Writing Secure Crypto Code

### A. Secure Random Token Generation

❌ Insecure

```python
''.join(random.choice(alphabet) for _ in range(length))
````

✅ Secure

```python
''.join(secrets.choice(alphabet) for _ in range(length))
# or simply:
secrets.token_urlsafe(length)
```

🔐 Use the `secrets` module — it's designed for cryptography.

---

## B. Salt Generation

❌ Insecure

```python
# Predictable, short, low-entropy salt
salt = ''.join(str(random.randint(0, 9)) for _ in range(21)) + '.'
```

✅ Secure

```python
salt = bcrypt.gensalt()
```

💡 Let libraries generate salts — they’ve already solved this problem securely.

---

### C. Password Hashing

❌ Insecure

```python
hashlib.md5(password.encode()).hexdigest()
```

✅ Secure

```python
bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```

⚠️ Avoid combining SHA256 and bcrypt unless you understand the risk tradeoffs. Bcrypt alone is slow and designed to defend against brute-force attacks.

---

### D. Secrets Management

❌ Insecure

```python
SECRET_KEY = 'TjWnZr4u7x!A%D*G-KaPdSgVkXp2s5v8'
```

✅ Secure

```python
SECRET_KEY = os.environ.get('SECRET_KEY')
```

🛑 Never commit secrets to source control — load them at runtime.

---

## 3. Fixing the Vulnerable Code

| Vulnerability   | Secure Fix                                      |
| --------------- | ----------------------------------------------- |
| `random.choice` | Use `secrets.choice` or `secrets.token_urlsafe` |
| Manual salt     | Use `bcrypt.gensalt()`                          |
| MD5             | Use `bcrypt.hashpw()`                           |
| Hardcoded keys  | Use `os.environ.get()` for key retrieval        |

---

## 4. Test-Driven Approach

### `tests.py` and `secure_tests.py`

The secure version includes tests to verify:

* Hashing and verification are correct
* Random tokens are unique and string-based
* Password verification fails with incorrect input
* Non-string inputs are safely rejected

### `hack.py`

In this level, `hack.py` reminds you that **CodeQL** or static analysis can help, but **isn't enough**. You must **choose the right algorithms**.

---

## 5. Training Your Brain for Cryptographic Safety

### Ask Yourself

| Area               | What to Look For                                                  |
| ------------------ | ----------------------------------------------------------------- |
| Randomness         | Is `random` used instead of `secrets`?                            |
| Salt Generation    | Is salt manually built or securely generated?                     |
| Hashing Algorithm  | Is bcrypt, PBKDF2, scrypt, or Argon2 being used?                  |
| Secret Management  | Are secrets loaded from the environment or config vault?          |
| Verification Logic | Are passwords verified using safe, timing-attack-resistant logic? |

---

### Best Practices

* Use libraries like `bcrypt`, `secrets`, or `argon2-cffi` — don’t DIY
* Never use MD5 or SHA1 for password storage
* Let your libraries generate salts and hashes
* Load secrets from environment variables or secure vaults
* Validate all inputs and types — fail securely

---

## Referenced Files

* `vulnerable_code.py`: Shows insecure randomness and hashing
* `secure_code.py`: Secure implementation
* `solution.py`: Teaching-focused patch
* `tests.py`: Validates secure behavior
* `hack.py`: Highlights importance of human code review
