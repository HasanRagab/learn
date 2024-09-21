
## **Week 1: Choosing OS and Setting Up Development Environment**

### **1. Choosing the Operating System**

- **Objective**: Help students select the right OS for software development.
- **Options**:
  - **Windows**: Good for general use but needs extra setup for dev work.
  - **Linux (Recommended)**: Ubuntu or other distributions are best for development.
  - **macOS**: Native UNIX environment, but costly.

### **Why Linux?**

- Open-source, developer-friendly.
- Many powerful CLI tools.
- The same environment as most production servers.

**Action**:

- Guide students to install **Ubuntu** or a beginner-friendly Linux distro (e.g., Linux Mint).
- Walkthrough installation using USB boot (provide resources on creating bootable USB drives).

---

### **2. Setting Up Development Environment**

#### **a. Terminal Basics**

- **Objective**: Get students comfortable using the terminal.
- **Skills to Cover**:
  - Opening the terminal (Ctrl+Alt+T for Linux, Terminal on macOS, PowerShell for Windows).
  - Basic commands: `ls`, `pwd`, `cd`, `mkdir`, `touch`.
- **Learning Task**: Create directories and files via terminal.

#### **b. Install Essential Tools**

- **Objective**: Install the most essential tools for development.

**Tools to Install**:

1.  **Code Editor**: Visual Studio Code (VS Code)

    - Install using the terminal:
      ```bash
      sudo apt update
      sudo snap install code --classic
      ```
    - Guide students to install extensions like ESLint, Prettier, and any language-specific extensions.
    - Log in to VS Code with GitHub account.

2.  **Git**:

    - **Git installation**:
      ```bash
      sudo apt install git
      ```
    - **Git setup**: Configure name and email.
      ```bash
      git config --global user.name "Your Name"
      git config --global user.email "your.email@example.com"
      ```

3.  **Node.js & npm** (JavaScript runtime):

    - Install Node.js via `nvm` (Node Version Manager):
      ```bash
      curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
      ```
      - Then install Node.js:
      ```bash
      nvm install node
      ```
      - Verify installation:
      ```bash
      node -v
      npm -v
      ```

4.  **Python** (Python 3):
    - Python is pre-installed on most Linux distributions.
    - Check version:
    ```bash
    python3 --version
    ```

#### **c. Setting Up Version Control**

- **Objective**: Familiarize students with version control basics.
- **GitHub**:

  - Create a GitHub account.
  - Set up SSH keys for secure pushing to GitHub:
    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```
    - Add the SSH key to GitHub.

- **Learning Task**: Create a GitHub repository, make an initial commit using `git add <file or pattern>`, `git commit -m "..."`, and `git push`.

---

### **3. Task for Week 1: First Project Setup**

- **Goal**: By the end of the week, students should have their environment set up and ready to start coding.
- **Task**:
  1.  Set up a GitHub repository named "my-first-project".
  2.  Create a folder and initialize it as a Git repository.
  3.  Push the empty folder to the GitHub repo using Git commands.
  4.  Install VS Code and practice creating files and folders via the terminal.
