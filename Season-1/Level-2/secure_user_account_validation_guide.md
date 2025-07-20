# Level 2 – Secure User Account Validation: Memory Safety & Defensive Programming

---

## 1. Understanding the Problem

**Context:**

- You have user accounts with admin flags, IDs, usernames, and a settings array.
- A function allows updating a setting via user-provided index.

**Goal:**  
Prevent privilege escalation or memory corruption through out-of-bounds indices.

**Questions to ask:**

- What memory is adjacent to user-writable arrays?
- Are negative or out-of-bounds indices possible?
- Can these be used to alter privilege or code flow?

---

## 2. Breaking Down the Solution(s)

### Key Concepts

- **Array Bounds Checking:**  
  Always check both lower (`i < 0`) and upper (`i >= SETTINGS_COUNT`) bounds before using as an array index.

- **Input Validation:**  
  Ensure index strings are valid integers with no trailing characters.

- **Struct Memory Awareness:**  
  Sensitive fields (like admin flags) before writable arrays are risky!

---

## 3. How the "Hack" Works and How the Solution Blocks It

- **The hack:** Uses a negative index (e.g., `-7`) to write to memory just before the settings array, flipping the `isAdmin` flag.

- **The secure solution:**
  - Checks `i < 0 || i >= SETTINGS_COUNT` before any write.
  - Ensures only intended fields are accessible via the update function.

---

## 4. Test-Driven Mindset

- **Standard tests** (`tests.c`): Confirm normal user logic works as intended.
- **Hack tests** (`hack.c`): Attempt to escalate privileges using negative indices—should be blocked by the secure fix.

---

## 5. How to Train Yourself for These Challenges

- List all possible values for user-supplied indices (including negatives and huge numbers).
- Check the struct layout: what’s adjacent to any user-writable fields?
- Imagine, test, and block every weird edge case.

---

## Summary Table: What to Focus On

| Area             | Questions to Ask / What to Look For              |
|------------------|--------------------------------------------------|
| Input Validation | Are indices both ≥0 and < SETTINGS_COUNT?        |
| Memory Layout    | Could a bad index write outside the array?       |
| Abuse Cases      | Could this lead to privilege escalation?         |
| Defensive Coding | Is every user input checked, every time?         |
| Testing          | Are hacks and edge cases covered?                |

---
