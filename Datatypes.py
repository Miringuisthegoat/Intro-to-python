age ="20" #Integer
length ="4.3" #float
greeting ="Hello there" #string
hasFeathers = True #Boolean

#Data Structures - Multiple Value stored in one variable

fruits =["Banana","Mango","Pineapple"]#list-ordered and changeable
courses =["MIT","Datascience","Cybersecurity"] #Array - Similar Datatypes
Cars =("Mercedes","Ford","Nissan","Toyota") #Tuple - ordered and unchangeable
Countries ={"Zambia","Canada","India","Jamaica","Netherlands"} #set - unordered and unchangeable
students ={
    "firstname" : "Esther",
    "course" : "MIT",
    "age" : 19,
    "Nationality" : "Kenyan",
    "Gender" : "Female"
} #Dictionary - Key value Pair

print(age)
print("The Length is",length)
print(fruits)
print(Countries)
print(students)
print(students["Nationality"])

#Typecasting - converting one datatype to another
print(int(length))