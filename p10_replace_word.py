# Step 1: Create a file with some text
with open('input.txt', 'w') as f:
    f.write("Gujarat is a state in India. "
             "Gujarat is known for its culture and heritage. "
             "Many people visit Gujarat for tourism.")

# Step 2: Read the contents of the file
with open('input.txt', 'r') as f:
    text = f.read()  # Read the entire file

# Step 3: Replace 'gujarat' with 'Gujrat'
modified_text = text.replace('Gujarat', 'Gujrat')  # Replace the word

# Step 4: Write the modified text back to the file
with open('input.txt', 'w') as f:
    f.write(modified_text)  # Write the new text to the file

print("All occurrences of 'Gujarat' have been replaced with 'Gujrat' in input.txt.")