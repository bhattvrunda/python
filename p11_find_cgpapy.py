# Step 1: Create a file with some grades
with open('grades.txt', 'w') as f:
    f.write("3.5\n")
    f.write("4.0\n")
    f.write("2.8\n")
    f.write("3.2\n")
    f.write("3.7\n")

# Step 2: Read the grades from the file
grades = []
with open('grades.txt', 'r') as f:
    for line in f:
        grades.append(float(line.strip()))  # Convert each line to float and add to the list

# Step 3: Compute the CGPA
if grades:  # Check if the list is not empty
    total_points = sum(grades)  # Sum all the grades
    cgpa = total_points / len(grades)  # Calculate CGPA
else:
    cgpa = 0.0  # If no grades, CGPA is 0

# Step 4: Display the CGPA
#it will give decimal values 
print(f"The CGPA is: {cgpa:.2f}")
