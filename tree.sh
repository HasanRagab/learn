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
