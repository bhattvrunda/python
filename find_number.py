#Find all mobile number out of long text
import re

# Step 1: Define a long text containing mobile numbers
text = """
Here are some mobile numbers:
John's number is 9876543210.
You can also reach me at 9123456789 or at 123-456-7890.
My office number is (123) 456-7890.
Don't forget to call me at +1-234-567-8901.
"""

# Step 2: Define a simple regex pattern to match mobile numbers
# This pattern looks for sequences of 10 digits
pattern = r'\d{10}|\d{3}[-.\s]?\d{3}[-.\s]?\d{4}'

# Step 3: Find all mobile numbers in the text
mobile_numbers = re.findall(pattern, text)

# Step 4: Print the extracted mobile numbers
print("Extracted mobile numbers:")
for number in mobile_numbers:
    print(number)



#import re

# Sample text containing mobile numbers
#text = """
#Here are some mobile numbers:
#John's number is 9876543210.
#You can also reach me at 9123456789 or at 123-456-7890.
#My office number is (123) 456-7890.
#Don't forget to call me at +1-234-567-8901.
#"""

# Regular expression pattern for matching 10-digit mobile numbers
# This pattern matches numbers with or without country code, with or without dashes or spaces
#pattern = r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'

# Find all mobile numbers in the text
#mobile_numbers = re.findall(pattern, text)

# Print the extracted mobile numbers
#print("Extracted mobile numbers:")
#for number in mobile_numbers
   # print(number)
