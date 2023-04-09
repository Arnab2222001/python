class Student:
    def _init_(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def _init_(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def get_average_grade(self):
        count = 0
        for i in self.students:
            count = count + i.get_grade()

        return count / len(self.students)    

s1 = Student("Ayan", 21, 100)    
s2 = Student("Meow", 20, 20)
s3 = Student("Doggy", 20, 100)

course = Course("Computer Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.get_average_grade())

class pet:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old ")    

class cat(pet):
    def sound(self):
        print("Meow")

class dog(pet):
    def sound(self):
        print("Woof")

class bird(pet):
    def sound(self):
        print("Koo")

c = cat("Hulo", 5)
c.show
c.sound
d = dog("Bhulo", 11)
d.show
d.sound
b = bird("Tia", 31)
b.show
b.sound

g = pet("Guinie", 2)
g.show
#g.sound