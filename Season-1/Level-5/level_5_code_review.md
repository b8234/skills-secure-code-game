# 📄 `level_5_code_review.md` – Secure Python Code Review: Level 5 – Cryptography & Randomness

````markdown
# Secure Python Code Review – Level 5: Cryptographic Safety & Randomness

---

## 1. What Is This Code Trying To Do?

The code implements core cryptographic utilities:

* Generates secure tokens (used for URLs, API keys, etc.)
* Hashes passwords using `SHA-256` or `MD5`
* Stores sensitive secrets (e.g., PRIVATE_KEY, SECRET_KEY)
* Verifies password authenticity

There are two key classes:
- `Random_generator`: handles randomness and salt generation
- `SHA256_hasher` and `MD5_hasher`: handle password hashing/verification

---

## 2. What’s the Risk?

The original implementation makes three critical mistakes:

| Concern                         | Issue                                                                 |
| ------------------------------ | --------------------------------------------------------------------- |
| Weak Randomness                | Uses `random.choice` for tokens — not cryptographically secure       |
| Predictable Salt               | Manually generates salt with `random.randint`                        |
| Broken Hashing Algorithm       | Uses **MD5**, a deprecated and insecure hashing algorithm            |
| Pre-hashing with SHA256 + bcrypt | May reduce bcrypt’s effectiveness by modifying its input             |

These mistakes expose passwords to offline brute-force or collision attacks.

---

## 3. Line-by-Line Review

### A. Insecure Token Generation

```python
# Insecure: random.choice is not suitable for security
''.join(random.choice(alphabet) for _ in range(length))
````

## ✅ Secure Fix: Salt Generation

```python
# Uses cryptographically secure randomness
''.join(secrets.choice(alphabet) for _ in range(length))
```

---

### B. Insecure Salt Construction

```python
# Insecure: manual, biased salt structure
salt = ''.join(str(random.randint(0, 9)) for _ in range(21)) + '.'
return f'$2b${rounds}${salt}'.encode()
```

### ✅ Secure Fix: Salt and Token Generation

```python
# Safe: uses bcrypt.gensalt()
return bcrypt.gensalt(rounds)
```

---

### C. Hashing with MD5

```python
# Known-insecure hash function
hashlib.md5(password.encode()).hexdigest()
```

### ✅ Secure Fix: Token Generation

```python
# Use bcrypt with SHA256-preprocessing (still controversial, but better)
password = binascii.hexlify(hashlib.sha256(password.encode()).digest())
bcrypt.hashpw(password, salt)
```

---

### D. Hardcoded Secrets

```python
# Insecure: hardcoded sensitive key in source code
SECRET_KEY = 'TjWnZr4u7x!A%D*G-KaPdSgVkXp2s5v8'
```

### ✅ Secure Fix

```python
# Secure: Load from environment variables
SECRET_KEY = os.environ.get('SECRET_KEY')
```

---

## 4. What Should Stand Out in Review

| Pattern                        | Good or Bad? | Why?                                        |
| ------------------------------ | ------------ | ------------------------------------------- |
| `random.choice()` for secrets  | ❌ Bad        | Not cryptographically secure                |
| Manual salt generation         | ❌ Bad        | Predictable, low entropy                    |
| MD5 password hashing           | ❌ Bad        | Easily reversible, fast, insecure           |
| bcrypt.gensalt() usage         | ✅ Good       | Secure, randomized salt                     |
| secrets.choice() usage         | ✅ Good       | Designed for cryptographic randomness       |
| `os.environ.get()` for secrets | ✅ Good       | Avoids committing secrets to source control |

---

## 5. Secure Coding Checklist: Crypto Edition

* [x] Are secure randomness functions (e.g. `secrets`) used?
* [x] Are salts generated using `bcrypt.gensalt()`?
* [x] Is MD5 avoided in favor of strong algorithms like bcrypt?
* [x] Are secrets managed via environment variables, not hardcoded?

---

## 6. Mantra

> “Random ≠ secure. Don't roll your own crypto. Use vetted libraries.”

---

## References

* `vulnerable_code.py`
* `secure_code.py`
* `solution.py`
* `tests.py` / `secure_tests.py`
* `hack.py`
