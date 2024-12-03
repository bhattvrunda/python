#Find all email addresses out of long text.
import re

text="""My departmental email id is rupesh@cse.iitm.ac.in. This is what i use for all the official purposes.
    This institute also provides an id rupesh@iitm.ac.in.
    During PHD ,i used to have a personal email ID rupesh0something@gmail.com,which is still in use.
    When gmail was not around id rupesh_something@usa.net was the one i used.
    I also own a twitter handle @rupedhsomething,which i hardly use.Thats it from my side for now. see you in class @11.
    """

regex=r'\w+@[\w\.]+'
emails=re.findall(regex,text.lower())
print(emails)



#Here is the 2nd way to find emails using regex
#import re

# Step 1: Define a long text containing email addresses
#text = """
#Here are some email addresses:
#You can reach me at example@example.com.
#For support, contact support@domain.org.
#My personal email is john.doe123@gmail.com.
#Don't forget to email info@website.net for inquiries.
#"""

# Step 2: Define a simple regex pattern to match email addresses
# This pattern looks for typical email formats
#pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Step 3: Find all email addresses in the text
#email_addresses = re.findall(pattern, text)

# Step 4: Print the extracted email addresses
#print("Extracted email addresses:")
#for email in email_addresses:
 #   print(email)
