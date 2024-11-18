def read_file(file_path):
    """Read the contents of a file and return it as a string."""
    try:
        with open(file_path, 'r') as file:
            return file.read()  # Read the entire file
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""

def split_text(text):
    """Split the text into words."""
    return text.split()  # Split the text into words using spaces

def write_sentences(words, output_file_path):
    """Write words as sentences to a new file."""
    with open(output_file_path, 'w') as file:
        for i in range(0, len(words), 5):  # Take 5 words at a time
            sentence = ' '.join(words[i:i+5])  # Join 5 words into a sentence
            file.write(sentence + '\n')  # Write the sentence to the file

# Main code execution
if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    # Create an example input file
    with open(input_file, 'w') as f:
        f.write("This is a simple example to demonstrate how to split text into words and join them to form sentences. "
                 "This program will read from one file and write to another file.")

    # Read the text from the input file
    text = read_file(input_file)

    # Split the text into words
    words = split_text(text)

    # Write the words as sentences to the output file
    write_sentences(words, output_file)

    print(f"Sentences have been written to {output_file}.")