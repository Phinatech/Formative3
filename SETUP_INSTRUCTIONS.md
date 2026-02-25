# Git Setup Instructions for Formative 3

## Repository Information
- **Repository URL**: https://github.com/Mukunzijames/Formative3.git
- **Main Branch**: main

## Team Member Branches
- **James Mukunzi**: `james/part1-probability-distributions`
- **Favor**: `favor/part2-bayesian-probability`
- **Chinemerem**: `chinemerem/part3-manual-gradient-descent`
- **Ryan**: `ryan/part4-coded-gradient-descent`

---

## For Ryan: Initial Setup and Push

### Step 1: Check Current Git Status
```bash
git status
```
This shows which files are untracked, modified, or staged.

### Step 2: Stage All New Files
```bash
git add .
```
Or to stage specific files only:
```bash
git add Formative3/
git add requirements.txt
```

### Step 3: Commit with Descriptive Message
```bash
git commit -m "Initial project setup: Add project structure, README, and contribution guidelines"
```

### Step 4: Push to Main Branch on GitHub
```bash
git push origin main
```
If this is your first push, you may need to set the upstream:
```bash
git push -u origin main
```

### Step 5: Verify the Push Was Successful
```bash
git log --oneline -n 5
```
Then check on GitHub: https://github.com/Mukunzijames/Formative3

You can also verify with:
```bash
git remote -v
git branch -a
```

---

## For Team Members: Clone and Create Branches

### Step 1: Clone the Repository
```bash
git clone https://github.com/Mukunzijames/Formative3.git
cd Formative3
```

### Step 2: Verify You're on Main Branch
```bash
git branch
git status
```

### Step 3: Create Your Feature Branch

**For James Mukunzi (Part 1: Probability Distributions):**
```bash
git checkout -b james/part1-probability-distributions
```

**For Favor (Part 2: Bayesian Probability):**
```bash
git checkout -b favor/part2-bayesian-probability
```

**For Chinemerem (Part 3: Manual Gradient Descent):**
```bash
git checkout -b chinemerem/part3-manual-gradient-descent
```

**For Ryan (Part 4: Coded Gradient Descent):**
```bash
git checkout -b ryan/part4-coded-gradient-descent
```

### Step 4: Push Your Branch to GitHub
```bash
git push -u origin <your-branch-name>
```

Example for Ryan:
```bash
git push -u origin ryan/part4-coded-gradient-descent
```

---

## Working on Your Branch

### Make Changes and Commit Regularly
```bash
# Check what files you've changed
git status

# Stage your changes
git add <filename>
# or stage all changes
git add .

# Commit with a descriptive message
git commit -m "Add probability distribution functions"

# Push to your branch
git push
```

### Keep Your Branch Updated with Main
```bash
# Switch to main branch
git checkout main

# Pull latest changes
git pull origin main

# Switch back to your branch
git checkout <your-branch-name>

# Merge main into your branch
git merge main
```

---

## Creating a Pull Request

### Step 1: Push Your Final Changes
```bash
git add .
git commit -m "Complete [your section]: [brief description]"
git push
```

### Step 2: Create Pull Request on GitHub
1. Go to: https://github.com/Mukunzijames/Formative3
2. Click on "Pull requests" tab
3. Click "New pull request"
4. Select your branch as the "compare" branch
5. Select "main" as the "base" branch
6. Click "Create pull request"
7. Add a descriptive title and description:
   - What you implemented
   - Any issues or notes
   - Reference the CONTRIBUTIONS.md file
8. Request review from team members
9. Click "Create pull request"

### Step 3: Address Review Comments
If team members request changes:
```bash
# Make the requested changes
git add .
git commit -m "Address review comments: [description]"
git push
```
The pull request will automatically update.

### Step 4: Merge After Approval
Once approved, click "Merge pull request" on GitHub.

---

## Useful Git Commands

### Check Remote Repository
```bash
git remote -v
```

### View Commit History
```bash
git log --oneline --graph --all
```

### See Differences
```bash
# See unstaged changes
git diff

# See staged changes
git diff --staged
```

### Undo Changes (Use Carefully!)
```bash
# Discard changes to a file
git checkout -- <filename>

# Unstage a file
git reset HEAD <filename>

# Undo last commit (keep changes)
git reset --soft HEAD~1
```

### Switch Branches
```bash
git checkout <branch-name>
```

### List All Branches
```bash
# Local branches
git branch

# All branches (including remote)
git branch -a
```

---

## Troubleshooting

### If Push is Rejected
```bash
# Pull the latest changes first
git pull origin <your-branch-name>

# Then push again
git push
```

### If You Have Merge Conflicts
1. Git will mark the conflicting files
2. Open the files and look for conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`
3. Edit the files to resolve conflicts
4. Stage the resolved files: `git add <filename>`
5. Complete the merge: `git commit`

### If You Need Help
```bash
git --help
git <command> --help
```

---

## Best Practices

1. **Commit often** with clear, descriptive messages
2. **Pull before you push** to avoid conflicts
3. **Never commit directly to main** - always use feature branches
4. **Test your code** before creating a pull request
5. **Review others' code** thoroughly and constructively
6. **Keep commits focused** - one logical change per commit
7. **Write meaningful commit messages** - explain what and why, not just what

---

## Questions?
Contact your team members or refer to:
- Git documentation: https://git-scm.com/doc
- GitHub guides: https://guides.github.com/
