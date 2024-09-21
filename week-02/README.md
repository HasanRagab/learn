## **Week 2: Learn Basic Terminal Commands**

---

### **1. Objective**
The goal for **Week 2** is to familiarize students with the terminal's command-line interface (CLI) to improve their efficiency in interacting with the system. Students will learn more advanced terminal commands, understand file permissions, and explore some basic shell scripting.

---

### **2. Terminal Command Basics: Level Up**

#### **a. Navigation and File Management**

- **Objective**: Build upon Week 1's basics with more advanced terminal commands.

- **New Commands to Learn**:
  1. `cp` - Copy files or directories:
     ```bash
     cp source_file destination
     ```
  2. `mv` - Move or rename files/directories:
     ```bash
     mv file_name new_location_or_name
     ```
  3. `rm` - Remove files or directories:
     ```bash
     rm file_name
     ```
     (Use `rm -r` for directories, but be cautious.)
  4. `cat` - View contents of a file:
     ```bash
     cat filename
     ```
  5. `man` - View the manual page for any command:
     ```bash
     man command_name
     ```
  6. `find` - Locate files or directories:
     ```bash
     find /directory -name "filename"
     ```
  7. `grep` - Search inside files for specific text:
     ```bash
     grep "text_to_search" filename
     ```

---

### **3. File Permissions**

#### **a. Understanding File Permissions**

- **Objective**: Teach students how to view and modify file permissions.

- **Basics**:
  1. Use `ls -l` to see permissions of files and directories. It will show something like:
     ```
     drwxr-xr-x 2 user group 4096 Oct 13 10:00 my_folder
     ```
     - **d**: Directory
     - **rwx**: Read, write, execute permissions for owner, group, others.

  2. **Changing Permissions**: Use the `chmod` command to change file permissions.
     - Example:
       ```bash
       chmod 755 my_folder
       ```

- **Learning Task**: Create a file, view its permissions, and modify them using `chmod`.

---

### **4. Shell Scripting Basics**

#### **a. Introduction to Shell Scripting**

- **Objective**: Learn the basics of shell scripting for automation.

- **Why Shell Scripting?**
  - Automate repetitive tasks.
  - Write custom scripts to improve productivity.

- **Simple Example**:
  ```bash
  #!/bin/bash
  echo "Hello, World!"
  ```
  - Save this to a `.sh` file, make it executable (`chmod +x filename.sh`), and run it with:
    ```bash
    ./filename.sh
    ```

- **Learning Task**: Create a basic script to automate creating directories and files.

---

### **5. Git Advanced**

#### **a. Branching and Merging**

- **Objective**: Teach students to work with multiple branches in Git.

- **Basics**:
  1. Create a new branch:
     ```bash
     git branch branch_name
     ```
  2. Switch to the new branch:
     ```bash
     git checkout branch_name
     ```
  3. Merge the branch into `main`:
     ```bash
     git checkout main
     git merge branch_name
     ```

- **Learning Task**: Create a new branch, make changes, and merge it back into the `main` branch.

---

### **6. Week 2 Task: Automate Folder Setup**

#### **a. Goal**
By the end of **Week 2**, students should be able to navigate the terminal efficiently, manage file permissions, automate tasks, and handle Git branches.

#### **b. Task**:
1. Create a script that:
   - Creates a new project directory.
   - Initializes a Git repository.
   - Creates necessary subdirectories (`src`, `tests`, etc.).
2. Push this project setup to GitHub.
