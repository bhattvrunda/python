import re

# List of months
months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')

# Create a regex pattern using the months
regex12 = '|'.join(months)
# This will match month names followed by an optional day and an optional year
findalregex = r'(' + regex12 + r'[a-z]*\s+\d{1,2})(,?\s?\d{2,4})?'

# Sample text (replace with your actual text)
text = "The events are scheduled for jan 12, 2022 and feb 5."

# Find all matching dates
dates = re.findall(findalregex, text.lower())
for onedate in dates:
    print(onedate[0].strip())  # Only print the first capture group (the date part)
