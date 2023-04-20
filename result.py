from grades import Grades
from student import Student
from teacher import Teacher

print()
print('Student')
s1 = Student('011', 'Arisgado', 'Mary Ann', 'Temple', 'Students', '2nd', 'BSCS', 'A')
print(s1.getName())
print(s1.getCourse())
print()

print()
print('Teacher')
t1 = Teacher('011', 'Arisgado', 'Mary Ann', 'Temple', 'Teacher', 'DCLIS', 'Instructor')
print(t1.getName())
print(t1.getDept())
print(t1.getPosition())
print()

g1 = Grades(90, 90, 90, 98)
g1.id = '001'
g1.lastname = 'Arisgado'
g1.firstname = 'Mary Ann'
g1.middlename = 'Temple'
g1.course = 'BSCS'
g1.year = '2'
g1.section = 'A'

print(g1.getName())
print(g1.getCourse())
print(g1.getAverage())
