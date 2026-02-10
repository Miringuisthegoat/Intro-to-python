# Task 1:Create the Class
#create a class called student with the following attributes : fullname,course,age and feespaid


class Student:
    def __init__(self, fullname, course, age, feespaid):
        self.fullname = fullname
        self.course = course
        self.age = age
        self.feespaid = feespaid


    def eat(self):
        print("Loves eating")

    def study(self):
        print("Loves studying")


#Task 2:Create multiple objects
#create at least three student objects from the same class with different values and display the same information


# Create student objects
student1 = Student("Alice Omondi", "Computer Science", 20, True)
student2 = Student("Brian Kinuthia", "Engineering", 22, False)
student3 = Student("Jessica Mutava", "Biology", 19, True)


print(student1.fullname, student1.course, student1.age, student1.feespaid)
student1.study()
print()

print(student2.fullname, student2.course, student2.age, student2.feespaid)
student2.study()
print()

print(student3.fullname, student3.course, student3.age, student3.feespaid)
student3.study()