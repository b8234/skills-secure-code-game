---

## Level 1 – Secure Order Validation Challenge

Welcome!
This challenge is designed to help you think like both a programmer **and** a security reviewer. You’ll learn why robust input validation, correct data types, and defensive coding matter—especially when handling money.

---

# Folder Structure & File Guide

```text
level1/
│
├── code.py                  # Starter (potentially vulnerable) implementation
├── secure_code.py           # Robust, secure solution (best practices)
├── solution.py              # Generalized solution with extra commentary
│
├── tests.py                 # Standard test cases (valid, invalid, edge)
├── hack.py                  # "Attack" test cases that try to break your code
├── hint.js                  # A gentle hint or nudge if you're stuck (no spoilers!)
│
├── order_validation_examples.md   # Code and explanation "reference card"
├── secure_order_validation.md     # Strategy guide: float vs decimal, defensive coding
├── train-your-brain.md           # Guide for reviewing code like a security pro
│
└── README.md                # You are here!
```

## Level 1 – Secure Order Validation Challenge

## **What does each file do?**

* **`code.py`** – The initial implementation (with known flaws). Good for learning what *not* to do!
* **`secure_code.py`** – The correct, robust, and secure solution using best practices.
* **`vulnerable_code.py`** – A solution that works but has slight vulunerabilities in real-world use cases.
* **`solution_notes.py`** – A general solution, plus detailed commentary on vulnerabilities and fixes.
* **`tests.py`** – Tests covering normal usage, errors, and edge cases.
* **`hack.py`** – Tests that simulate attacks and exploitation attempts.
* **Documentation files** (`order_validation_reference.md`, `secure_order_validation_guide.md`, `secure_code_review_mindset.md`) – Quick reference, conceptual background, and mindset training.

---

## 🗝️ **Key Learnings from This Challenge**

After working through this exercise, you should be able to:

### 1. **Understand the Risks of Using Floats for Money**

* Floating-point math (using `float`) is *not* precise enough for currency.
* Even simple sums like `0.1 + 0.2` can lead to errors.
* **Use `Decimal`** for any calculation involving money.

### 2. **Validate All User Inputs**

* Never trust user input—**check type and range for every field**.
* Only allow expected item types (`'payment'` or `'product'`).
* Quantities must be positive integers, within sane limits.
* Amounts must be numbers, and also within allowed limits.

### 3. **Enforce Business Logic Strictly**

* A payment must pay for the products—no more, no less.
* Don’t allow tricks like negative payments or buying a fractional product.
* Limit maximum values for amounts and quantities to prevent abuse.

### 4. **Defend Against Edge Cases and Attacks**

* Hackers may try to:

  * Use huge numbers, negative values, or weird types.
  * Exploit rounding errors.
  * Rearrange items to trick the code.
* **Write “attack” tests** to see if your code holds up!

### 5. **Adopt a Secure Coding Mindset**

* Always ask: *“What could go wrong here?”*
* Imagine creative abuse cases and test them.
* Document your thinking and checks—your future self (or a teammate) will thank you.

---

## 🧠 **Practice Questions to Cement Your Skills**

* What happens if a user enters a string for the amount?
* How would your code react to a fractional or negative quantity?
* What’s the risk of allowing floats in currency fields?
* Can you write a test that would have failed the vulnerable implementation, but passes with the secure solution?

---

## 🚦 **How to Use This Folder**

1. **Start with `code.py`**.
   See how flaws can creep into a naive implementation.

2. **Explore `secure_code.py` and `solution_notes.py`**.
   Notice the use of `Decimal` and strict validation.

3. **Run `tests.py` and `hack.py`**.
   See which cases are handled—and which ones break.

4. **Review the markdown docs** for:

   * Practical code examples and explanations
   * Security mindset and defensive programming tips

5. **Practice extending the tests or adding your own exploits**.
   The best way to learn is to try to break things (and then fix them!).

---

## ⭐ **Takeaway**

> **Write code that’s not just “correct,” but secure, robust, and ready for the real world.**
> Always validate inputs, use the right data types, and test like a hacker!
