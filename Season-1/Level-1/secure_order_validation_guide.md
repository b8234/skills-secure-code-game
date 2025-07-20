# Level 1 – Secure Order Validation: Float vs Decimal & Defensive Programming

---

## 1. **Understanding the Problem: What is this code trying to solve?**

* **Context**: You have an "Order" with multiple "Items." Each item is either a product (something you buy) or a payment (money paid for products, or possibly a refund).
* **Goal**: Implement a function that verifies if an order is valid:

  * Are item types and amounts valid?
  * Do payments and products match (no under/over payment)?
  * Are totals within allowed business constraints (e.g., no giant payments or weird quantities)?
  * Is the order free of tricks or exploits?

**Questions you should train your brain to ask:**

* What are the *business rules* for this system? (What is supposed to be allowed, what isn't?)
* What *inputs* might a normal user vs. a malicious actor try to submit?
* What types of bugs or attacks are common in money-related code?

---

## 2. **Breaking Down the Solution(s)**

### **Key Concepts and Techniques to Notice**

* **Data Validation**: Each function is careful to check that `type`, `amount`, and `quantity` fields are within expected types and ranges.
* **Financial Calculations**: The `Decimal` type is used instead of floats to avoid rounding errors. (Why? See below.)
* **Order Logic**: Checks if total payments match total product cost and if order totals are within a cap.

### **Vulnerabilities to Train Yourself To Spot**

* **Floating Point Math**: Using floats with money is risky (`0.1 + 0.2 != 0.3` in Python). Always prefer `Decimal` for currency.
* **Input Tampering**: Allowing weird quantities (e.g., buying "1.5 TVs"), negative payments, or enormous numbers.
* **Order of Operations**: The order you process payments and products can matter for attacks.

---

## 3. **How the "Hack" Works and How the Solution Blocks It**

* The hack tries to "walk away" with a product by making a huge payment and an equally huge negative payment (refund), tricking a naive sum into thinking the order is balanced—even though no real money changed hands.
* A robust solution:

  * Limits the **range** of allowed amounts and quantities.
  * Validates **types** (e.g., no floats for quantity, only integers).
  * Uses **Decimal** for precise math.

---

## 4. **Test-Driven Mindset**

Notice the structure of the tests (`tests.py` and `hack.py`):

* Tests for valid payments, missing payments, refunds, invalid item types, invalid quantities, and "hacking" attempts.
* **Question**: What else would you test if you were the author? Think about edge cases and "weird" inputs.

---

## 5. **How to Train Yourself for These Challenges**

Here's a systematic approach you can use for any coding challenge—especially security or validation-related:

### **A. Always start with "What could go wrong?"**

* List **edge cases** and **abuse cases**.
* Example: What if the amount is negative, the quantity is zero, or a payment is huge?

### **B. Read every line with "Why?"**

* Why is this check here?
* What would happen if it was missing or wrong?

### **C. Look for "Trust" and "Assumptions"**

* Does the code trust user input? Should it?
* Is it assuming only well-behaved users? (Never do that!)

### **D. Look for "Type Safety"**

* Are types strictly enforced, especially for money and counts?
* Is anything implicitly cast, or allowed to be a float/string when it should be an integer/Decimal?

### **E. Think in Terms of "Business Logic"**

* Are the business rules fully represented in the code?
* What rules are not being enforced?

### **F. Test Like a Hacker**

* How would you try to break this? Try it!
* Would you try weird types, huge numbers, negative numbers, or rearrange items?

---

## 6. **What You Can Practice (Brain Training)**

* **Write tests for edge cases**: Try to invent new, "creative" ways to break the system and see if the code stops you.
* **Review security "gotchas"**: Research why floating-point math is dangerous for money.
* **Refactor for clarity and safety**: Practice converting any calculation involving money to use `Decimal`.
* **Ask "Is this logic airtight?"**: If you can imagine an attack, try it and see if you can plug the hole.

---

## 7. **Level-Up Thought Process for Python Coders**

* **Always use precise data types for money**.
* **Never trust input, ever**. Validate *everything*.
* **Design for failure**: Always ask yourself, "How could this fail? How could it be abused?"
* **Document your logic**: When you implement a fix, explain *why* it's there.
* **Write tests that cover normal and abnormal usage**.

---

## **Summary Table: What to Focus On**

| Area                  | Questions to Ask / What to Look For                  |
| --------------------- | ---------------------------------------------------- |
| Input Validation      | Are all types and values checked?                    |
| Business Rules        | Are limits enforced on prices, quantities, payments? |
| Floating Point Issues | Is Decimal used for money?                           |
| Abuse Cases           | What would a malicious user try?                     |
| Defensive Programming | Are weird cases and bad inputs safely handled?       |
| Testing               | Are tests comprehensive? What else would I add?      |

---
