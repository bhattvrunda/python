import shutil

# Function to print the contents of a file
def print_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Function to copy a file
def copy_file(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print(f"Copied {source_path} to {destination_path}")
    except FileNotFoundError:
        print(f"File not found: {source_path}")

# Function to read and write to a file
def read_and_write_file(file_path, new_content):
    try:
        with open(file_path, 'a') as file:  # Open in append mode
            file.write(new_content)
            print("New content added to the file.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Main code execution
if __name__ == "__main__":
    original_file = 'example.txt'
    copied_file = 'copied_example.txt'
    
    # Create an example file
    with open(original_file, 'w') as f:
        f.write("Hello, this is a sample file.\n")

    # Print the contents of the original file
    print("Original file contents:")
    print_file_contents(original_file)

    # Copy the original file
    copy_file(original_file, copied_file)

    # Append new content to the original file
    read_and_write_file(original_file, "\nThis is new content added to the file.")

    # Print the contents of the copied file
    print("\nCopied file contents:")
    print_file_contents(copied_file)