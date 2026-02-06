#functions/methods - a block of code used to perform a task


# 1. Standard - library/inbuilt functions

y = max(56,57,345,213,5666,6776,6545,2344)
print(y)

x = min(56,67,23,78)
print(x)

#User-defined functions
def school():
    print("eMobilis")

school()#calling a function


#parameters/variables
def multiply(x,y):
    print(x * y)

#Python program to display details of five employees at eMobilis
#use a user defined function with the help of parameters and arguments
#details- Fullname,Position,Age and gender





def show_employee(fullname, position, age, gender):
    print("Full Name :", fullname)
    print("Position  :", position)
    print("Age       :", age)
    print("Gender    :", gender)
    print("-------------------------")


show_employee("Ann Njeri", "Software Developer", 27, "Female")
show_employee("Brian Otieno", "Data Analyst", 30, "Male")
show_employee("Carol Mwangi", "Trainer", 35, "Female")
show_employee("David Kimani", "System Administrator", 32, "Male")
show_employee("Esther Ali", "UI/UX Designer", 25, "Female")
