# DSA in Python

**A structured data structures and algorithms learning journal by Rinvi Jaman Riti.**

I am building my foundations in problem solving using Python. This repository records my **independently written** solutions, the algorithmic patterns I learn, complexity analysis, mistakes, and revisions. My longer-term goal is to prepare for software engineering interviews and develop strong engineering fundamentals.

> **Status:** Starter repository. The practice problem solutions have intentionally not been added yet. I will upload them as I solve them.

## My approach

1. Learn the pattern, then attempt the problem without a solution video.
2. Write and test my own code; use hints only when needed.
3. Record time/space complexity and mistakes in the solution header.
4. Re-solve challenging problems after 3–7 days.
5. Keep Git commits meaningful: learning progress over activity streaks.

## Repository map

| Location | Purpose |
|---|---|
| [`exercises/`](exercises/README.md) | Topic folders, prompts and my future solutions |
| [`examples/`](examples/) | Small worked demonstrations of Python/algorithm fundamentals |
| [`tests/`](tests/) | Automated tests for worked examples and completed solutions |
| [`notes/`](notes/) | Algorithm patterns, complexity notes, solution template and interview log |
| [`PROGRESS.md`](PROGRESS.md) | Milestones and progress checklist |
| [`progress.csv`](progress.csv) | Problem-level practice and revision log |
| [`study-log/`](study-log/) | Weekly reflections |
| [`ROADMAP.md`](ROADMAP.md) | Twelve-week study sequence |

## Starting plan — Week 1

- Review Python lists, dictionaries, sets, and functions.
- Understand the difference between an `O(n)` scan and an `O(n²)` nested-loop solution.
- Solve **Contains Duplicate**, **Valid Anagram**, and **Two Sum**, in that order.
- For every solution, write a short explanation, time/space complexity and 2–3 tests.
- Review each solution from memory later in the week.

**Problem links and detailed instructions:** [`exercises/01-arrays-and-hashing/README.md`](exercises/01-arrays-and-hashing/README.md)

## Run the example tests

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

On Windows, activate with `.venv\Scripts\activate` instead.

The tests initially cover a **worked linear-search example**, not unfinished LeetCode exercises. As I implement new algorithms, I will add tests for those solutions too.

## Commit convention

Examples:
- `docs: record week 1 learning goals`
- `solve: add independently written contains duplicate solution`
- `test: add edge cases for two sum`
- `notes: revise hash map complexity explanation`

## Academic integrity

Solutions represent my own work. When I learn an idea from external material, I credit that source and explain it in my own words. Problem statements belong to their respective platforms; this repository links to them rather than reproducing them in full.

## Learning resources

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [CS50P](https://cs50.harvard.edu/python/)
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [LeetCode](https://leetcode.com/problemset/)
