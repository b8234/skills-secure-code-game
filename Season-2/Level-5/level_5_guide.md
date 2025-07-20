# 📄 `level_5_guide.md`

````markdown
# 📄 `level_5_guide.md`

## Level 5 – JavaScript Pitfalls: Type Coercion, Prototype Abuse & Internal Exposure

---

## 1. Understanding the Problem

### Context

This level simulates vulnerabilities in a client-side JavaScript SHA-1 implementation (`CryptoAPI.sha1.hash`) that lacks type enforcement and internal encapsulation.

The code:
- Accepts an input (`s`) and processes it for SHA-1 hashing
- Uses user input directly, assuming it behaves like a string
- Exposes internal methods like `_round`, and uses a regular array without isolation

---

### Issue

```text
Multiple attack vectors arise from JavaScript's flexibility:

| Component           | Flaw                                                       |
|--------------------|------------------------------------------------------------|
| Input Handling      | Accepts any object, leading to coercion via `toString()`  |
| Internal Exposure   | `_round` method is public and overrideable                |
| Data Structure      | Uses standard arrays susceptible to prototype pollution   |

---
````

## 2. Key Concepts: Securing JavaScript APIs

### A. Input Type Validation

✅ Enforce string inputs:

```js
if (typeof input !== "string") throw new TypeError("Expected string input");
```

❌ Blind coercion allows object exploitation:

```js
CryptoAPI.sha1.hash({ toString: () => alert("Exploit!") });
```

---

### B. Protect Internal Logic

✅ Copy internal references into a local closure:

```js
var internalRound = API.sha1._round;
```

❌ Trusting `API.sha1._round` is unsafe — it can be overwritten.

---

### C. Defend Against Array Prototype Abuse

✅ Preinitialize or isolate data structures:

```js
var w = Object.create(null);
```

Or:

```js
var w = new Array(128).fill(0);
```

❌ Using `[]` allows prototype extension via `__defineSetter__`.

---

## 3. Fixing the Vulnerable Code

```text
| Vulnerability       | Secure Fix                                      |
|---------------------|-------------------------------------------------|
| Type Coercion       | Check `typeof input === "string"`               |
| Method Overwrite    | Use internal closure copy of `_round`           |
| Prototype Tampering | Use `Object.create(null)` or prefill arrays     |

---
```

## 4. Test Coverage

### `hack-*.js`

* Exploit 1: Abuse of `toString()` on input object
* Exploit 2: Overwrites `_round` with malicious function
* Exploit 3: Uses `__defineSetter__` to hijack array assignment

---

## 5. Training Your Brain

```text
| Area           | Ask Yourself                                                       |
|----------------|--------------------------------------------------------------------|
| Input Handling | Are we validating the type before using it?                        |
| API Exposure   | Are internal functions or fields exposed to user manipulation?     |
| Prototype Use  | Could `Array.prototype` or `Object.prototype` be leveraged here?   |
| Function Scope | Are we referencing internal functions securely (closure vs object)?|

---
```

## Referenced Files

* `code.js` – insecure CryptoAPI
* `secure_code.js`, `vulnerable_code.js` – before/after versions
* `hack-1.js`, `hack-2.js`, `hack-3.js` – exploit simulations
* `hint-*.txt` – guidance
