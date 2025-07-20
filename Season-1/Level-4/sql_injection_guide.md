# Level 4 – SQL Injection Defense: Parameterization and Input Validation

---

## 1. Understanding the Problem

### Context

The original `code.py` defined a `DB_CRUD_ops` class to interact with a stock database. It provided methods to:

* Fetch stock info
* Retrieve stock price
* Update stock price
* Execute arbitrary queries (via `exec_multi_query` and `exec_user_script`)

### Issue

Several of these methods directly interpolated **user input into SQL strings**, leading to SQL Injection vulnerabilities.

### What is SQL Injection?

An attacker manipulates query logic by injecting malicious SQL code into user-supplied input fields. This can lead to:

* Data manipulation (e.g., `UPDATE`, `DELETE`, `DROP`)
* Unauthorized access to sensitive records
* Full database corruption

---

## 2. Key Concepts: Writing Secure SQL Code

### A. Parameterized Queries

Instead of doing this (vulnerable):

```python
query = f"SELECT * FROM stocks WHERE symbol = '{user_input}'"
cur.execute(query)
```

You should always do this (safe):

```python
query = "SELECT * FROM stocks WHERE symbol = ?"
cur.execute(query, (user_input,))
```

### B. Input Validation

The secure solution validates the stock symbol before executing any query:

```python
symbol.isalnum() and symbol.isupper() and len(symbol) <= 5
```

### C. Query Logging (Test Compatibility vs Security)

To support legacy tests and secure production behavior, the secure implementation supports two modes:

* `secure` (only logs parameterized queries)
* `compatible` (interpolates safely for test comparison)

---

## 3. Fixing the Vulnerable Code

### A. Vulnerable Example

```python
query = "SELECT price FROM stocks WHERE symbol = '" + stock_symbol + "'"
cur.executescript(query)
```

### B. Secure Fix in `secure_code.py`

```python
cur.execute("SELECT price FROM stocks WHERE symbol = ?", (symbol,))
```

And validates the symbol first:

```python
if not self._is_safe_symbol(symbol):
    return "CONFIRM THAT THE ABOVE QUERY IS NOT MALICIOUS TO EXECUTE"
```

---

## 4. Test-Driven Development Approach

### `tests.py`

Validates secure behavior:

* Good inputs succeed
* Malicious inputs return confirmation prompt

### `hack.py`

Simulates malicious attempts:

* SQL Injection attempts are blocked or confirmed as unsafe

---

## 5. Training Your Brain for SQL Injection Challenges

### Ask Yourself

| Area               | What to Look For                                     |
| ------------------ | ---------------------------------------------------- |
| Query Composition  | Are SQL statements built using string interpolation? |
| Parameter Binding  | Are queries parameterized using placeholders?        |
| Input Sanitization | Are inputs validated for length, charset, format?    |
| Execution Methods  | Are `executescript()` or unfiltered queries used?    |
| Output Logging     | Are logs interpolating unsafe input directly?        |

### Best Practices

* Never concatenate user input into SQL.
* Always use prepared statements with parameter binding.
* Validate user input before query execution.
* Avoid designing methods that execute raw user input (e.g., `exec_user_script`).

---

## Referenced Files

* `vulnerable_code.py`: Original insecure implementation
* `secure_code.py`: Secure, testable design with validation
* `tests.py`: Validates expected behavior
* `hack.py`: Simulates SQL injection
* `solution.py`: Teaching aid for parameterized defense pattern
