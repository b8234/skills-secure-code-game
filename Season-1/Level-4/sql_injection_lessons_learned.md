# Level 4 – SQL Injection Defense: Lessons Learned

---

## 1. What Went Wrong in the Original Code

### The Problem

The initial `code.py` implemented logic like:

```python
query = "SELECT * FROM stocks WHERE symbol = '" + stock_symbol + "'"
cur.executescript(query)
```

This form of string-based SQL execution is vulnerable to **SQL injection**, especially when user inputs contain control characters like `';` or `--`.

### The Offenders

* **get\_stock\_info** and **get\_stock\_price**: interpolated raw strings
* **update\_stock\_price**: used string formatting with no type enforcement
* **exec\_multi\_query** and **exec\_user\_script**: allowed full arbitrary logic execution

---

## 2. Dangerous Design Patterns

### `exec_multi_query()` and `exec_user_script()`

These methods allowed users to execute multiple SQL commands directly. Even with minimal restrictions, this exposes a wide attack surface:

```python
query = "SELECT price FROM stocks WHERE symbol = 'MSFT'; DROP TABLE stocks;--"
```

**Lesson:** *If your method lets users define entire SQL statements, you’ve already lost.*

---

## 3. How the Exploit Works (from `hack.py`)

```python
op.get_stock_price("MSFT'; UPDATE stocks SET price = '525' WHERE symbol = 'MSFT'--")
```

In vulnerable code, this would:

* Bypass intended logic
* Chain a second command using `;`
* Silently mutate data or delete tables

---

## 4. How the Secure Fix Solves It

### SecureStockDB Class

* Introduces parameterized SQL
* Validates input format via `_is_safe_symbol()`
* Rejects unvalidated inputs with a clear response

### Logging Mode

Supports both `secure` and `compatible` modes:

```python
[QUERY] SELECT * FROM stocks WHERE symbol = ?
```

---

## 5. Takeaways

| Vulnerability Area | Mistake Made                     | Secure Alternative                     |
| ------------------ | -------------------------------- | -------------------------------------- |
| Query Construction | Direct string concatenation      | Use parameterized queries (`?`)        |
| Input Trust        | Assumed all input was safe       | Validate symbol format with rules      |
| Execution Function | Used `executescript()`           | Use `execute()` with parameters        |
| Design             | Allowed arbitrary SQL from users | Remove dynamic query execution methods |

---

## 6. Key Reminders

* Assume user input is malicious
* Use database parameterization always
* Never give users the power to define logic
* Validate symbols: length, charset, and case
* Review logs and test for exploit cases

---

### Files That Show the Journey

* `code.py`: insecure starting point
* `hack.py`: shows what can go wrong
* `solution.py`: explains best practices
* `secure_code.py`: robust and safe design
* `tests.py`: validates secure behavior
