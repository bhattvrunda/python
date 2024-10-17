#Practicle3=Print a liat recursively
# Define a recursive function to print items in a list
def print_list(lst, index=0):
    # Base case: if index is equal to the length of the list, stop recursion
    if index == len(lst):
        return
    # Print the current element
    print(lst[index])
    # Recursive call with the next index
    print_list(lst, index + 1)

# Example usage
my_list = [10, 20, 30, 40, 50]
print_list(my_list)
