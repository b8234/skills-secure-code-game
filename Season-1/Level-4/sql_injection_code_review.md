# Secure Python Code Review – Level 4: SQL Injection Defense

---

## 1. What Is This Code Trying To Do?

The application implements a small stock database with three core actions:

* Get stock info by symbol
* Retrieve current stock price
* Update a stock price

It initially used direct SQL query composition, which allowed input like this:

```python
"MSFT'; DROP TABLE stocks--"
```

and would execute malicious commands.

The refactored `SecureStockDB` class:

* Uses safe parameterized queries
* Validates all inputs
* Supports secure and test-friendly logging

---

## 2. Line-by-Line: Trust, Validate, Guard

### A. Original Code: Interpolation

```python
query = "SELECT * FROM stocks WHERE symbol = '" + stock_symbol + "'"
```

* Directly injects user input into SQL logic.
* Unsafe: any special characters or SQL keywords are executed.

### B. Secure Fix: Parameterized

```python
cur.execute("SELECT * FROM stocks WHERE symbol = ?", (symbol,))
```

* Input is treated strictly as data
* No way for user input to alter the SQL logic

### C. Validation Check

```python
def _is_safe_symbol(self, symbol):
    return symbol.isalnum() and symbol.isupper() and len(symbol) <= 5
```

* Ensures symbols are uppercase, short, and alphanumeric
* Prevents malformed inputs from reaching the DB layer

---

## 3. Compatible vs Secure Logging

To support test case expectations:

```python
log_mode = 'secure' | 'compatible'
```

### `secure` Mode

```python
[QUERY] SELECT price FROM stocks WHERE symbol = ?
```

### `compatible` Mode

```python
[QUERY] SELECT price FROM stocks WHERE symbol = 'MSFT'
```

This preserves legacy test output formatting without compromising security.

---

## 4. What Should Stand Out in Review

| Pattern                      | Good or Bad? | Why?                                                        |
| ---------------------------- | ------------ | ----------------------------------------------------------- |
| `executescript()`            | ❌ Bad        | Allows execution of multiple commands at once               |
| Raw string formatting        | ❌ Bad        | Susceptible to injection attacks                            |
| `execute()` + `?`            | ✅ Good       | Forces DB to treat input as data only                       |
| Input validation             | ✅ Good       | Rejects malformed or suspicious inputs                      |
| Separate query logging logic | ✅ Good       | Allows traceability without reverting to insecure practices |

---

## 5. Secure Coding Checklist: SQL Edition

* [x] Are all queries using parameterized statements?
* [x] Are dangerous APIs like `executescript()` avoided?
* [x] Is user input validated for format and length?
* [x] Is test logging separated from execution logic?
* [x] Are results tested for both safe and unsafe inputs?

---

## 6. Mantra

> "User input is hostile until proven harmless. Parameterize everything. Trust nothing."

---

## References

* `vulnerable_code.py`
* `secure_code.py`
* `tests.py`
* `hack.py`
* `secure_test_runner.py`
