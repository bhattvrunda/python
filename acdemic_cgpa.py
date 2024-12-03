#Create a module to track academic performance.
#steps:
#1.Add a new course along with its total creadits and earned points.
#2.Drop a course
#3.Print Whole academic record.
#4.know the current CGPA=sum of(credits*points)/sum of credits

from academics import *

# Initialize lists
courses = []
credits = []
earned = []

def add(cc, cr, ea):
    courses.append(cc)
    credits.append(cr)
    earned.append(ea)

def drop(cc):
    index = courses.index(cc)
    courses.pop(index)
    credits.pop(index)
    earned.pop(index)

def cprint():
    print("course", "credits", "earned")
    for ii in range(len(courses)):
        print(courses[ii], credits[ii], earned[ii])

def cgpa():
    numerator = denominator = 0
    for ii in range(len(credits)):
        cr = credits[ii]
        ea = earned[ii]
        numerator += cr * ea
        denominator += cr

    # Avoid division by zero
    return numerator / denominator if denominator != 0 else 0

# First semester
add("CS1100", 9, 10)
add("CS1200", 12, 9)
add("AM1100", 9, 9)
cprint()
print("1st SEM CGPA:", cgpa(), "\n")

# Second semester
add("EE2101", 12, 8)
add("CS2200", 12, 10)
drop("EE2101")
add("CS2310", 6, 10)
add("CS2710", 6, 9)
cprint()
print("2nd SEM CGPA:", cgpa(), "\n")