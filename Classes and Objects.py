class Student:
    #Class Variable - `Have Same Value for all objects
    school = "Longfield School"

    #Instance Variable - Have Different Values for all Objects
    def __init__(self, name, age, year, birthday):
        self.name = name
        self.age = age
        self.year = year
        self.birthday = birthday

#Creating Objects
student1 = Student("James", 10, 6, "1/1/1")
print(student1.school)
print(student1.name)
print(student1.age)

student2 = Student("Jack", 12, 8, "2/2/2")
print(student2.school)
print(student2.name)
print(student2.age)