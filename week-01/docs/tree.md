### **Creating a Simple Tree Command**

- **Objective**: Teach students how to create a simple shell script that mimics the `tree` command to display directory structures in a hierarchical format.

#### **Concepts to Cover**:

1. **Understanding the `tree` Command**:

   - The `tree` command lists files and directories in a tree-like format, making it easier to visualize the structure of a directory.

2. **Using Recursion**:

   - Introduce the concept of recursion to navigate through directories and list their contents.
   - Discuss how to call the script recursively to handle subdirectories.

3. **Indentation for Hierarchy**:

   - Use spaces or special characters (like `|` and `--`) to create visual indentation that represents the directory structure.

4. **Handling Command-Line Arguments**:
   - Allow the user to specify the starting directory as an argument.
   - If no argument is given, default to the current directory.

#### **Learning Task**:

- Write a script that takes a directory path as an argument and prints the directory structure in a tree-like format.
- Implement a recursive function to traverse the directory.

#### **Example Script**:

```bash
#!/bin/bash

# Function to print the directory structure
print_tree() {
    local dir=$1
    local prefix=$2

    # List all files and directories in the current directory
    for item in "$dir"/*; do
        if [ -d "$item" ]; then
            echo "${prefix}|-- $(basename "$item")"  # Print the directory name
            print_tree "$item" "$prefix    "         # Recursive call
        elif [ -f "$item" ]; then
            echo "${prefix}|-- $(basename "$item")"  # Print the file name
        fi
    done
}

# Main script execution
start_dir=${1:-.}  # Use the provided argument or default to current directory
echo "Directory structure of $start_dir:"
print_tree "$start_dir" ""
```

[tree.sh](./tree.sh).

### **Usage**:

- Save the script as `tree.sh`.
- Make it executable: `chmod +x tree.sh`.
- Run the script with an optional directory argument:
  - To view the current directory: `./tree.sh`
  - To view a specific directory: `./tree.sh /path/to/directory`
