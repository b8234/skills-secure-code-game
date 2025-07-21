# 🧠 Season 5 – Level 1: Prompt Injection – Leaking a Gift Code

Welcome to Level 1 of Season 5 of the Secure Code Game!

In this level, you'll explore how a **large language model (LLM)** can be tricked into revealing sensitive information—even when it has strict instructions not to.

---

## 🎯 Objective

Your goal is to write a clever `userPrompt` that **bypasses the AI’s guardrails** and gets it to reveal a secret gift card code. The system message includes clear restrictions, but with the right phrasing, you can convince the model to give up the full code.

---

## 🧩 What’s Provided

### 📁 `code.spec.js`
This test file simulates a chat between a user and the LLM. It contains:
- A system message embedding the secret (`${SECRET}`)
- A vulnerable prompt masking rule (e.g. `*****U1N8`)
- Your `userPrompt` — where the magic happens

✅ Modify the `userPrompt` to trick the LLM  
❌ Do not modify the system message

### 📄 `hint.txt`
Provides subtle advice:  
> Avoid direct questions. Use misdirection, synonyms, or social engineering.

---

## 🛠️ How to Run

You can run this level using:

```bash
npm --prefix Season-3 run test:Level-1
```

Or click ▶️ next to the `test()` block in `code.spec.js`.

---

## 📚 Strategy Guide

See the following markdown files to help craft your attack:

| File                     | Purpose                                            |
|--------------------------|----------------------------------------------------|
| `level_1_guide.md`       | Strategic breakdown of how to approach the problem |
| `level_1_code_review.md` | Analysis of what made the prompt vulnerable        |
| `level_1_lessons_learned.md` | Final reflection and secure design takeaways     |

---

## 🔐 Key Learning

> Just because an LLM has instructions doesn’t mean it’s safe.

You’ll learn how LLMs can be socially engineered and how prompt injection can lead to secret leaks—an increasingly important topic in AI security.

---

## ✅ Success Criteria

You’ll know you’ve succeeded when:

```
✅ Congratulations! You've successfully made the LLM leak a gift code! 🎉
```

---

## 📎 Reminder

Once you pass, **do not "fix" the system prompt yet**. The objective is to identify the vulnerability first — not to patch it.

---
