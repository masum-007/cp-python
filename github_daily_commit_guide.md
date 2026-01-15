# GitHub Daily Commit Guide for Competitive Programming

This is a **ready-to-use step-by-step guide** for maintaining your GitHub repository for LeetCode and Codeforces problems. You can push your daily progress and light up your GitHub contribution calendar.

---

## 1️⃣ Prerequisites

1. Install **Git** and verify:
```bash
git --version
```
2. Have a **GitHub account**.
3. Install **VS Code**.
4. (Optional) Install **GitHub VS Code extension** for easy integration.

---

## 2️⃣ Create a Repository

1. Go to [GitHub](https://github.com/) → **New Repository**.
2. Name: `competitive-programming-python`.
3. Public or Private.
4. Click **Create repository**.

---

## 3️⃣ Clone the Repository

```bash
git clone https://github.com/YourUsername/competitive-programming-python.git
```

Open the folder in VS Code.

---

## 4️⃣ Organize Folder Structure

```
competitive-programming-python/
│
├── leetcode/
│   ├── easy/
│   ├── medium/
│   └── hard/
│
├── codeforces/
│   ├── 800/
│   ├── 1000/
│   └── 1200/
│
└── templates/
    ├── leetcode.py
    └── codeforces.py
```

- One file per problem.
- Clear names: `two_sum.py`, `cf_sample_problem.py`.

---

## 5️⃣ Write Problem Code

- Create a new `.py` file in the proper folder.
- Paste your solution.
- Use optimized versions whenever possible.

---

## 6️⃣ Stage Your Changes

```bash
git add .  # Adds all new/modified files
```
Or specific file:
```bash
git add leetcode/easy/two_sum.py
```

---

## 7️⃣ Commit Your Changes

Use clear, consistent daily messages:

```bash
git commit -m "Solved 1 LeetCode + 0 Codeforces problems"
```

Optional with problem names:

```bash
git commit -m "Solved Two Sum (LC) + 0 CF problems"
```

Multiple problems in a day:

```bash
git commit -m "Solved 3 LeetCode + 2 Codeforces problems"
```

---

## 8️⃣ Push to GitHub

```bash
git push origin main
```

- Your GitHub repo updates.
- Contribution calendar lights up.

---

## 9️⃣ Daily Workflow

1. Solve problems in VS Code.
2. Add new files.
3. Stage files:
```bash
git add .
```
4. Commit with daily message.
5. Push:
```bash
git push origin main
```

- Repeat daily.
- Optional: Track your daily numbers.

---

## 🔟 Optional Pro Tips

1. Keep **code clean** and optimized.
2. Do not delete old files → shows progress.
3. Separate folders → easier navigation.
4. Optional: Maintain a README with total solved:
```
Total LeetCode solved: 50
Total Codeforces solved: 30
```
5. One commit per day → consistent green squares.

---

## Example Commit Messages

| Day | Commit Message |
|-----|----------------|
| 1   | Solved 1 LeetCode + 0 Codeforces problems |
| 2   | Solved 2 LeetCode + 1 Codeforces problem |
| 3   | Solved 3 LeetCode + 2 Codeforces problems |

---

Follow this guide every day to build a **professional and consistent GitHub profile** for competitive programming.

