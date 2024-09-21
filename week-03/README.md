## **Week 3: Learn Git and GitHub**

---

### **1. Objective**

In **Week 3**, students will focus on mastering version control using Git and GitHub. They will go beyond basic commands to learn about collaboration, resolving conflicts, and working with pull requests.

---

### **2. Git Fundamentals Review**

#### **a. Recap of Basic Git Commands**

- **Objective**: Ensure a solid understanding of basic Git commands.
- **Commands**:
  1. `git init` - Initialize a new Git repository.
  2. `git add` - Stage changes for the next commit.
  3. `git commit` - Commit staged changes with a message.
  4. `git status` - View the status of the working directory.
  5. `git log` - View commit history.
  6. `git push` - Upload local commits to a remote repository.
- **Learning Task**: Review these commands by making a few changes in a project, staging, committing, and pushing them to a GitHub repository.

---

### **3. Branching, Merging, and Conflict Resolution**

#### **a. Branching Revisited**

- **Objective**: Teach students how to work in isolated environments and merge changes.
- **Commands**:
  1. **Create and switch branches**:
     ```bash
     git checkout -b new-branch
     ```
  2. **View all branches**:
     ```bash
     git branch
     ```

#### **b. Merging Branches**

- **Objective**: Help students understand how to combine changes from different branches.
  - Switch to the main branch:
    ```bash
    git checkout main
    ```
  - Merge changes from `new-branch`:
    ```bash
    git merge new-branch
    ```

#### **c. Conflict Resolution**

- **Objective**: Teach students how to resolve conflicts when merging branches.

  - If a conflict occurs during merging, Git will pause and notify about the conflicting files.
  - Open the conflicting file, resolve the conflict manually, and stage the changes:
    ```bash
    git add conflict_file
    git commit
    ```

- **Learning Task**:
  1. Create a branch, make changes in both `main` and the new branch.
  2. Merge the branches and intentionally create a conflict.
  3. Resolve the conflict and commit the merge.

---

### **4. Working with Remotes and Collaborating**

#### **a. Setting Up Remote Repositories**

- **Objective**: Understand how to link local repositories to remote ones.
  - View the current remotes:
    ```bash
    git remote -v
    ```
  - Add a new remote repository:
    ```bash
    git remote add origin https://github.com/username/repo.git
    ```

#### **b. Cloning Repositories**

- **Objective**: Learn how to clone a repository from GitHub.
  ```bash
  git clone https://github.com/username/repo.git
  ```

#### **c. Fetching and Pulling Changes**

- **Objective**: Teach the difference between fetching and pulling.

  1. **Fetch**: Download changes from the remote repository without merging.
     ```bash
     git fetch
     ```
  2. **Pull**: Fetch and automatically merge changes into the current branch.
     ```bash
     git pull
     ```

- **Learning Task**: Set up a remote for a project and practice pushing/pulling changes.

---

### **5. Collaboration on GitHub**

#### **a. Forking and Pull Requests (PRs)**

- **Objective**: Learn how to contribute to other projects through forks and pull requests.
  1. **Fork a repository** on GitHub and clone it locally.
  2. **Make changes** and push them to your fork.
  3. Create a **pull request** on GitHub, proposing your changes to the original repository.

#### **b. Reviewing and Merging PRs**

- **Objective**: Learn how to review code changes and collaborate with others using GitHub's PR feature.

  - Leave comments on a pull request.
  - Request changes or approve the PR.
  - Merge the PR once approved.

- **Learning Task**:
  1. Fork a public repository.
  2. Make changes and submit a pull request.
  3. Review a classmate’s pull request and merge it if appropriate.

---

### **6. Week 3 Task: Collaborative Git Project**

#### **a. Goal**

By the end of **Week 3**, students should feel confident in using Git and GitHub for both solo and collaborative work.

#### **b. Task**:

1. Create a group project repository on GitHub.
2. Collaborate by creating branches for different features.
3. Merge changes, resolve conflicts, and submit pull requests.
