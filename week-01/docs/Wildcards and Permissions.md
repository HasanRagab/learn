### **Wildcards: `*`, `?` for Searching and Pattern Matching**

Wildcards are special characters used in Unix/Linux systems to represent patterns in filenames, allowing for flexible searching or file operations. The two most common wildcards are `*` and `?`.

1. **`*` (Asterisk)**:

   - The `*` wildcard matches **zero or more characters** in a filename.
   - Example:
     - `ls *.txt` will list all files with the `.txt` extension in the current directory, such as `file1.txt`, `report.txt`, etc.
     - `rm file*` will delete all files whose names start with `file`, such as `file1`, `fileA.txt`, etc.

2. **`?` (Question Mark)**:
   - The `?` wildcard matches **exactly one character** in a filename.
   - Example:
     - `ls file?.txt` will match filenames like `file1.txt` or `fileA.txt` but **not** `file10.txt` (since `?` only matches one character).
     - `rm file?.txt` will remove files with names like `file1.txt`, `file2.txt`, etc.

Together, these wildcards can help in pattern matching during file manipulation, searches, or when running commands.

### **File Permissions: `chmod`, `chown`, `chgrp`**

File permissions in Linux determine who can read, write, or execute a file or directory. These permissions are managed with the commands `chmod`, `chown`, and `chgrp`.

#### **1. `chmod` (Change Mode)**

The `chmod` command is used to change file or directory permissions.

- **Syntax**: `chmod [permissions] [file]`
- File permissions are represented by three categories:
  1. **Owner** (user)
  2. **Group**
  3. **Others**

Each permission can be:

- `r`: Read
- `w`: Write
- `x`: Execute

Permissions can be set using symbolic (letters) or numeric (octal) representation.

- **Symbolic**:

  - `chmod u+x file`: Adds execute permission (`x`) for the user (owner).
  - `chmod g-w file`: Removes write permission (`w`) for the group.
  - `chmod o=r file`: Sets read-only permission for others.

- **Numeric (Octal)**:
  - Permissions are represented by numbers: `4` (read), `2` (write), `1` (execute).
  - Example: `chmod 755 file`
    - `7` (Owner) = Read (4) + Write (2) + Execute (1) = `rwx`
    - `5` (Group) = Read (4) + Execute (1) = `r-x`
    - `5` (Others) = Read (4) + Execute (1) = `r-x`

#### **2. `chown` (Change Owner)**

The `chown` command is used to change the ownership of a file or directory.

- **Syntax**: `chown [new-owner] [file]`
- Example:
  - `chown user1 file`: Changes the owner of the file to `user1`.
  - `chown user1:group1 file`: Changes the owner to `user1` and the group to `group1`.

#### **3. `chgrp` (Change Group)**

The `chgrp` command changes the group ownership of a file or directory.

- **Syntax**: `chgrp [new-group] [file]`
- Example:
  - `chgrp developers file`: Changes the group ownership of `file` to `developers`.

### **Summary**

- **Wildcards**:
  - `*` matches zero or more characters.
  - `?` matches exactly one character.
- **Permissions**:
  - `chmod` changes permissions (read, write, execute).
  - `chown` changes file ownership.
  - `chgrp` changes the group ownership.
