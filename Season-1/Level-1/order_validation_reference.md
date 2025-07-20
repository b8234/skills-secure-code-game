# Level 1 – Order Validation: Real Examples & Lessons Learned

---

## 1. `code.py` – The Starter (Potentially Vulnerable) Implementation

### Example: Payment Imbalance Detection (but with floats)

```python
EPSILON = 0.0001

def validorder(order: Order):
    # ... (init code) ...
    net = total_payments - total_products
    if abs(net) > EPSILON:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    # ...
```

**Why it works:**

* It tries to handle tiny rounding errors with `EPSILON` (float safety).

**Why it’s risky:**

* Still relies on floating-point math for money!
* Attackers can exploit float rounding bugs (e.g., `0.1 + 0.2 != 0.3`), or extremely large/small values may behave unexpectedly.

**Example Exploit:**

* In `hack.py` test\_6, an attacker pays with a huge amount, then immediately refunds the same huge amount, which can cause overflow/underflow or slip past float checks.

---

## 2. `secure_code.py` – The Robust, Secure Implementation

### Example: Use of Decimal for Money (Avoids Floating-Point Bugs)

```python
from decimal import Decimal, InvalidOperation

def validorder(order: Order) -> str:
    total_products = Decimal('0')
    total_payments = Decimal('0')
    for item in order.items:
        try:
            amount = Decimal(str(item.amount))
        except (InvalidOperation, TypeError, ValueError):
            return f"Invalid amount: {item.amount}"
        # ... rest of validation ...
```

**Why it works:**

* **Decimal arithmetic** is exact for money, no float rounding errors!
* All inputs converted to strings before Decimal, so you avoid float imprecision.

### Example: Strict Input Validation

```python
if not isinstance(item.quantity, int):
    return f"Invalid quantity type: {item.quantity} ({type(item.quantity)})"
if item.type == 'product':
    if not (MIN_QUANTITY <= item.quantity <= MAX_QUANTITY):
        return f"Quantity out of range: {item.quantity}"
elif item.type == 'payment':
    if item.quantity != 1:
        return f"Payments must have quantity 1, got: {item.quantity}"
```

**Why it works:**

* Rejects non-integer or out-of-range quantities (prevents buying "1.5 TVs" or "a million TVs").
* Payments can only have quantity 1.

### Example: Catches the Hack

* In `hack.py`, the attacker pays \$1e19, then refunds -\$1e19, trying to zero out the balance but actually receives a product for free.
* **This solution stops it** because:

  * Payments and products must both be within allowed ranges.
  * Payment must be exactly the right total, no games with quantity/amount.
  * All logic uses `Decimal` so no rounding bugs.

---

## 3. `solution.py` – Commentary and Generalized Defenses

### Example: Range Checking and Use of Decimal

```python
MAX_ITEM_AMOUNT = 100000
MAX_QUANTITY = 100
MIN_QUANTITY = 0
MAX_TOTAL = 1e6

def validorder(order):
    payments = Decimal('0')
    expenses = Decimal('0')
    for item in order.items:
        if item.type == 'payment':
            if -MAX_ITEM_AMOUNT <= item.amount <= MAX_ITEM_AMOUNT:
                payments += Decimal(str(item.amount))
        elif item.type == 'product':
            if type(item.quantity) is int and MIN_QUANTITY < item.quantity <= MAX_QUANTITY and MIN_QUANTITY < item.amount <= MAX_ITEM_AMOUNT:
                expenses += Decimal(str(item.amount)) * item.quantity
        else:
            return "Invalid item type: %s" % item.type
    # ... more checks ...
```

**Why it works:**

* No payment or product can be too big or negative (anti-overflow/abuse).
* Quantities and amounts are strictly controlled.

**Why this is secure:**

* **Prevents edge-case exploits:** Even if attacker tries huge/negative numbers, the system blocks it.
* **Decimal everywhere:** No float math for money.
* **Catches all weird input:** e.g., product with float quantity, negative values, etc.

---

## 4. Test & Hack Files – Learning Through Examples

* **tests.py**: Covers good orders, missing payments, refunds, invalid types, and non-integer quantities.
* **hack.py**: Demonstrates a creative attack by using massive numbers for payments/refunds (the vulnerable solution would fail here, but secure ones pass).

### Example: Hack Attempt (from `hack.py`)

```python
tv_item = c.Item(type='product', description='tv', amount=1000.00, quantity=1)
payment = c.Item(type='payment', description='invoice_4', amount=1e19, quantity=1)
payback = c.Item(type='payment', description='payback_4', amount=-1e19, quantity=1)
order_4 = c.Order(id='4', items=[payment, tv_item, payback])
self.assertEqual(c.validorder(order_4), 'Order ID: 4 - Payment imbalance: $-1000.00')
```

* **The Secure Solution returns "Payment imbalance" and blocks the order**.

---

## 5. Reference Table: What Works and Why

| Example from Code         | Why it Works / Fails                                   | Lesson for You                      |
| ------------------------- | ------------------------------------------------------ | ----------------------------------- |
| Float with EPSILON        | Can still have rounding bugs, imprecise for money      | Never use float for money           |
| `Decimal` for All Money   | Exact, no rounding errors                              | Always use `Decimal` for currency   |
| Strict Type Checks        | Prevents weird/invalid quantities or negative values   | Validate all inputs, by type/range  |
| Range Checking            | No crazy big or small numbers slip through             | Set max/min for money and quantity  |
| "One Payment per Payment" | Stops payment quantity exploits                        | Check business rules, not just math |
| Edge/Hack Tests           | Demonstrates what can go wrong and ensures it's caught | Always test abuse cases             |

---

## Your Documentation "Cheat Sheet"

### When Writing Code That Handles Money

1. **Never trust user input** – validate everything!
2. **Use `Decimal`, not float** for all calculations.
3. **Set reasonable max/min on all amounts and quantities**.
4. **Check for weird types** – e.g., no floats for quantity, no string for amount.
5. **Business rules matter** – payment logic, product logic, etc.
6. **Write tests that mimic attacks** – the more creative, the better.

---

### Practice Prompts to Cement These Lessons

* What would happen if a user entered a string for the amount? For quantity?
* How would you write a test to ensure negative payments are rejected?
* Can you write a test that tries to exploit floats, and see how your code responds?

---

If you want specific examples for documentation, here’s how you might phrase them:

> **Example: Use of Decimal**
> *In `secure_code.py`, every amount is wrapped with `Decimal(str(item.amount))`. This ensures calculations are exact, and blocks all floating-point rounding errors that could be used to exploit the system.*
>
>
> **Example: Strict Quantity Check**
> *Payments must have quantity 1. Products must have an integer quantity between 1 and 100. This blocks both fractional purchases and payment multiplication tricks.*

---

Let me know if you want these expanded as code comments, visual diagrams, or a checklist for your own code reviews!
