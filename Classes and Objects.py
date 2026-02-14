class Student:
    #Class Variable - `Have Same Value for all objects
    school = "Longfield School"

    #Instance Variable - Have Different Values for all Objects
    def __init__(self, name, age, year, birthday):
        self.name = name
        self.age = age
        self.year = year
        self.birthday = birthday

    def result(self, maths_mark, english_mark, science_mark, history_mark, geography_mark):
        total = maths_mark + english_mark + science_mark + history_mark + geography_mark
        entire_score = 500
        percentage = total/entire_score*100
        print("Total score is " + str(total))
        print("Percentage is " + str(percentage) +"%")



#Creating Objects
student1 = Student("James", 10, 6, "1/1/1")
print(student1.school)
print(student1.name)
print(student1.age)
student1.result(83, 92, 87, 76, 89)


student2 = Student("Jack", 12, 8, "2/2/2")
print(student2.school)
print(student2.name)
print(student2.age)
student2.result(95, 73, 85, 81, 79)