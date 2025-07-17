# Git & GitHub Notes

A personal reference for useful Git and GitHub commands, workflows, and troubleshooting tips discovered during my learning journey.

---

## 📦 Basic Git Commands

- `git status`  
  See the current state of your working directory and staging area.
- `git add <filename>`  
  Stage changes for commit.
- `git add .`  
  Stage all changed files.
- `git commit -m "your message"`  
  Commit staged changes with a message.
- `git log`  
  View commit history.
- `git diff`  
  See changes not yet staged.
- `git diff --staged`  
  See changes staged for the next commit.

---

## 🚀 Working With Remotes

- `git remote -v`  
  List remote repositories.
- `git push`  
  Push commits to the default remote repository.
- `git pull`  
  Fetch and merge changes from the remote.
- `git clone <url>`  
  Clone a repository.

---

## 🌳 Branching

- `git branch`  
  List local branches.
- `git checkout -b <branch-name>`  
  Create and switch to a new branch.
- `git checkout <branch-name>`  
  Switch to an existing branch.
- `git merge <branch-name>`  
  Merge another branch into the current one.

---

## 🛠️ Troubleshooting & Tips

- **"No staged changes to commit"**  
  - Remember to run `git add` before `git commit`.
- **Undo last commit (keep changes):**  
  - `git reset --soft HEAD~1`
- **Discard local changes:**  
  - `git checkout -- <filename>`
- **Remove file from staging:**  
  - `git reset <filename>`

---

## 📝 Commit Message Guidelines

- For learning log and notes:  
  - `docs: update learning log with today's notes`
  - `log: add troubleshooting steps for Codespaces`
- For code updates:  
  - `feat: practice Python dictionaries`
  - `fix: correct typo in print statement`

---

## 🌐 GitHub Tips

- Use Issues for tracking learning goals or questions.
- Use Pull Requests to review and merge changes from feature branches.
- [GitHub Docs](https://docs.github.com/en) for official help.

---

_Add more notes here as you learn new commands or workflows!_