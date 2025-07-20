# Secure Python Code Review – Brain Training Guide for Coders

## 1. Start with a Calm Overview

**First thought:**  
*What is this code supposed to do?*

- We have `Order`s, which are lists of `Item`s.
- Each `Item` is either a **product** (something bought) or a **payment** (money paid).
- The function `validorder` should check if the money paid exactly covers the things bought (and nothing else sneaky is going on).

---

## 2. Read Each Line and Say What it Does (Out Loud or in Your Head)

**Ask yourself for every line/block:**

- “What does this do?”
- “What does it expect?”
- “What could go wrong?”

**Example:**

```python
for item in order.items:
    if item.type == 'payment':
        net += item.amount
    elif item.type == 'product':
        net -= item.amount * item.quantity
    else:
        return "Invalid item type: %s" % item.type
````

**Thoughts:**

- For payments, add to `net` (that’s money coming in).
- For products, subtract the cost (`amount * quantity`) from `net` (that’s money going out).
- If the item isn’t a payment or product, error.

---

## 3. Look for “Holes” — Where Could This Go Wrong?

### a) Input Types

- **Are `amount` and `quantity` always numbers?**
  What if someone sends a string, or a negative, or even `float("nan")`?
- **Should `quantity` ever be negative or non-integer?**
  Usually, you can’t buy -3 or 0.5 of an item in real life!

### b) Limits

- **Is there a maximum amount or quantity?**
  If not, what if someone buys 1,000,000,000 items or pays \$999999999?
- **Are negative payments allowed?**
  Should a user be able to “reverse” a payment by just using a negative number?

### c) Floating Point

- **Is `amount` a float?**
  *Big Red Flag!* Floats aren’t exact for money (e.g., `0.1 + 0.2 != 0.3`).
  **Should you use `Decimal` instead?** YES!

### d) Comparison

- **How is the code checking if paid == owed?**
  `if net != 0:` could fail if rounding errors sneak in.

---

## 4. Imagine Sneaky Test Cases

*Pretend to be a “bad guy” or just a curious user. Try these in your head:*

- What if I pay \$1,000,000 and buy \$1?
- What if I use 0.0001 as an amount?
- What if I use a fractional quantity, like 0.1?
- What if I do `amount = float('nan')` or `float('inf')`?
- What if I pay negative money?

---

## 5. How Would I Fix These?

*Ask yourself:*

- Should I check the type and range for each value? (Yes)
- Should I make sure only positive integers are used for `quantity`? (Yes)
- Should I limit `amount` and `quantity` to sane values? (Yes)
- Should I switch from `float` to `Decimal` for money? (Yes)
- Should I use something like `abs(net) < EPSILON` for comparing money? (Or, better, compare using Decimals, which are precise.)

---

## 6. What Would My New Validation Look Like?

**Walk through your thinking:**

- For every item:

  - If it’s not a payment or product, reject it.
  - If `amount` isn’t a number, reject it.
  - If `quantity` isn’t a *positive integer*, reject it (for products).
  - If `amount` or `quantity` is way too big or negative, reject it.
  - If using for money, use Decimal for all calculations.

**After looping through items:**

- Make sure the totals make sense.
- If paid != owed, return an error.
- If amounts are over a maximum, return an error.

---

## 7. Key Questions to Train Your Brain

- **What’s the happy path (normal user flow)?**
- **What are the “danger paths” (how could someone break it)?**
- **Am I validating every input before using it?**
- **Is my data type appropriate for what I’m doing?**
- **What are my edge cases?**

---

### 🧠 Secure Coding Mantra

> “Trust nobody. Validate everything. Use the right types for the right job. Always imagine how things could break, not just how they work.”

---
