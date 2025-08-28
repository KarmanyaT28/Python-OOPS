class Student:
    stdCount = 0

    def __init__(self, name,grade):
        self.name=name
        self.grade=grade

        Student.stdCount +=1


    @staticmethod
    def showCount():
        print(Student.stdCount)


s1 = Student("Karmanya",'A')
s2 = Student("Aanyaa",'A')

print(s1.stdCount)
Student.showCount()
        