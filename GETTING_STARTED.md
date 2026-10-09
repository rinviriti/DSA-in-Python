# Getting started (MacBook / terminal)

## 1. Create the empty repository on GitHub

1. Sign in to [github.com/rinviriti](https://github.com/rinviriti).
2. Go to **+** > **New repository**.
3. Use `DSA-in-Python` as the name and choose **Public**.
4. **Do not** add a README, .gitignore or license on the GitHub site; these are already in the starter package.
5. Create the empty repository.

## 2. Unzip this starter package and push it

Open **Terminal** in the extracted `DSA-in-Python` folder:

```bash
cd /path/to/DSA-in-Python
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q

git init
git add .
git commit -m "chore: initialize DSA learning repository"
git branch -M main
git remote add origin https://github.com/rinviriti/DSA-in-Python.git
git push -u origin main
```

If Git requests credentials, sign in using GitHub's supported authentication flow (or use GitHub Desktop). Never paste access tokens into repository files.

If you already initialized the folder as a Git repository, skip `git init` and check existing remotes with `git remote -v`.

## 3. Add your first independently solved problem

- Read `exercises/01-arrays-and-hashing/README.md`.
- Create `exercises/01-arrays-and-hashing/contains_duplicate.py`.
- Use `notes/SOLUTION_TEMPLATE.md` as an explanation checklist.
- Write a unit test in `tests/` and run `python -m pytest -q`.
- Update `progress.csv` and `PROGRESS.md`.
- Commit and push:

```bash
git add .
git commit -m "solve: contains duplicate with hash set"
git push
```

## Troubleshooting

- `python3: command not found`: install Python 3 and use the terminal for your installation.
- `pytest: command not found`: run `python -m pytest` after activating the environment.
- `git: command not found`: install Xcode Command Line Tools (`xcode-select --install`) on macOS.
- Authentication failure: configure GitHub CLI/GitHub Desktop or an appropriate Git credential manager.
