# Troubleshooting.md

## Issue #1: Branch Not Published Before Merge

### Description:
I created a new branch called `<feature-addition>` and made changes to it. However, before I could publish the `feature-addition` branch to the remote repository, I attempted to merge it with the `main` branch. The merge went through successfully, and the `main` branch updated with the changes, but the `feature-addition` branch was not visible because it had not been published yet.

### Cause:
The issue occurred because I merged the `feature-addition` branch into `main` before publishing the `feature-addition` branch to the remote repository. As a result, the `main` branch was updated with the changes, but the `feature-addition` branch was not available in the remote repository, and I couldn't see it.

### Resolution:
Yulisa helped identify that I had not published the `feature-addition` branch. To resolve this:
1. I published the `feature-addition` branch by pushing it to the remote repository.
2. Once the branch was pushed, I was able to see it and verify the changes.

### Fix:
To avoid similar issues in the future:
1. Always ensure that branches are published to the remote before attempting to merge them.
2. Use the `git push` command or GitHub Desktop to push the branch and ensure it is available remotely.

---


## Issue #2: Reverted a Commit Due to an Error

### Description:
I made an error by modifying the `README.md` file with incorrect information. Specifically, I committed the following incorrect text:

"lkiuyghasdrefgyluiasdgbyhjulifjhgbysaedjbghyfdjhbn,aswebn hawsfbhj njhbn afesjhbn"


After committing this change, I realized it was a mistake and needed to revert it.

### Cause:
The error was a random and nonsensical string of characters that shouldn't have been in the `README.md`. Once I reviewed the change, I decided it needed to be undone.

### Resolution:
I reverted the commit using GitHub Desktop. This created a new commit that undid the changes from the previous commit.

### Fix:
To avoid similar issues in the future:
1. Always review changes carefully before committing.
2. Use the 'Revert This Commit' option in GitHub Desktop to safely undo a commit when an error is identified after committing.

---
