# 📄 `level_5_code_review.md`

````markdown
# 📄 `level_5_code_review.md`

## Secure Code Review – Level 5: JS Object Coercion, Internal Exposure, Prototype Abuse

---

## 1. What Is This Code Trying To Do?

The `CryptoAPI.sha1.hash()` function computes a SHA-1 hash in JavaScript.

It accepts an input, converts it to a binary representation, and processes it in 512-bit blocks using a SHA-1-style compression function (`_round`).

---

## 2. What’s the Risk?

```text
| Concern                | Issue                                                       |
|------------------------|-------------------------------------------------------------|
| Type Coercion          | Accepts any object, trusting implicit `toString()` behavior |
| Internal API Exposure  | `_round()` is public and can be overwritten externally      |
| Array Exploits         | Prototype setter abuse via `__defineSetter__()`             |

---
````

## 3. Line-by-Line Review

### A. No Input Type Check

```js
// ❌ Dangerous: coerces objects via toString()
CryptoAPI.sha1.hash({ toString: () => alert("Exploit!") });
```

```js
// ✅ Fix: Ensure input is a string
if (typeof input !== "string") throw new Error("Expected string input");
```

---

### B. Internal Method Exposure

```js
// ❌ _round is accessible and overrideable
CryptoAPI.sha1._round = () => alert("Exploit!");
```

```js
// ✅ Fix: Use closure-scoped internal copy
var internalRound = API.sha1._round;
```

---

### C. Prototype Setter Abuse

```js
// ❌ Exploitable via __defineSetter__("0", maliciousFunction)
var w = [];
```

```js
// ✅ Secure: isolate prototype
var w = Object.create(null);
```

Or:

```js
var w = new Array(128).fill(0);
```

---

## 4. Secure Coding Checklist

* [x] Enforce input type expectations
* [x] Avoid exposing internal APIs
* [x] Initialize arrays defensively
* [x] Never trust `Object.prototype` or `Array.prototype` to be safe

---

## 5. Mantra

> “Validate input, isolate logic, and protect the prototype chain.”

---

## References

* `code.js`, `secure_code.js`, `vulnerable_code.js`
* `hack-1.js`, `hack-2.js`, `hack-3.js`
