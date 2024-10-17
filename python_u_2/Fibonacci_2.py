#print fibbonaci string E.g:('A','B','BA','BAB','BABBA')
# Function to generate Fibonacci strings
def fibonacci_strings(n):
    # Start with the first two Fibonacci strings
    fib_strings = ['A', 'B']
    
    # Generate Fibonacci strings until we reach the desired count
    for i in range(2, n):
        next_string = fib_strings[i - 1] + fib_strings[i - 2]  # Combine the last two strings
        fib_strings.append(next_string)  # Add the new string to the list

    return fib_strings

# Number of Fibonacci strings to generate
n = 5
fib_strings = fibonacci_strings(n)

# Print the Fibonacci strings
for s in fib_strings:
    print(f"'{s}'")
