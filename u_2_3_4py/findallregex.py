import re
text=""" Hello,my phone number is 9940533241.Otherwise you call my assistance at 8932732436.I am available at clinic from 9 to 1.For appoinment ,call reception at (687)324-3234."""
digits10=r"\d{10}"

regex=digits10
mobile=re.findall(regex,text)
print(mobile)
