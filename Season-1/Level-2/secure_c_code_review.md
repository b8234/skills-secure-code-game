# Secure C Code Review – Brain Training Guide for Coders  

## Level 2: Memory Safety

---

## 1. Start with a Calm Overview

**First thought:**  
*What is this code supposed to do?*

- We have **user accounts**, each with a username, an admin flag, and an array of user settings.
- Functions allow you to **create accounts**, **update settings**, and **check privileges**.
- **The goal:** Prevent users from gaining unintended admin privileges or corrupting other user data by exploiting memory layout.

---

## 2. Read Each Line and Say What It Does

For each line or code block, ask yourself:

- **What does this do in memory?**
- **Does it trust user input?**
- **What could go wrong if an index or pointer is abused?**

**Example:**

```c
long i = strtol(index, &endptr, 10);
if (*endptr)
    return false;
if (i < 0 || i >= SETTINGS_COUNT)
    return false;
accounts[user_id]->setting[i] = v;
````

- What happens if `index` is negative or out of bounds?
- What field is just before the array in memory?

---

## 3. Look for “Holes” — Where Could This Go Wrong?

- **Input Types:**
  Are indices validated to only access the intended settings, not other fields?

- **Memory Layout:**
  Are sensitive fields (like `isAdmin`) placed right before user-modifiable arrays?

- **Array Bounds:**
  Does the code check **both lower and upper bounds** for all array accesses?

- **Pointers:**
  Could a `user_id` or pointer be `NULL` or invalid?

---

## 4. Imagine Sneaky Test Cases

- What if I use `-7` as a settings index?
- What if I provide an index greater than `SETTINGS_COUNT - 1`?
- What if `user_id` is out of bounds?

---

## 5. How Would I Fix These?

- **Always check:** `i < 0 || i >= SETTINGS_COUNT` **before using any index.**
- **Validate all input**, including pointer validity (e.g., ensure `accounts[user_id]` is not `NULL`).
- **Design structs defensively:** Avoid placing sensitive fields directly before or after arrays that users can write to.

---

## 6. Key Questions to Train Your Brain

- Is the index or user input **strictly validated** for both range and type?
- Could writing to this array **corrupt other fields** (e.g., escalate privileges)?
- Are **all memory and privilege boundaries** clearly enforced?

---

## 🧠 Secure Coding Mantra

> “Trust nobody. Validate everything. Always imagine how memory could be misused—not just how it works in the happy path.”

---
