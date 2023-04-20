from grades import Grades
from teacher import Teacher

students = []
teachers = []


def addStudents():
    while True:
        print()
        print('Enter student information')
        id = input('Enter ID: ')
        lastname = input('Enter Last_name: ')
        firstname = input('Enter First_name: ')
        middlename = input('Enter Middle_name: ')
        type = input('Enter type: ')
        course = input('Enter Course: ')
        year = input('Enter Year: ')
        section = input('Enter Section: ')
        print('-------------------------------------------')
        filipino = input('Grade Filipino: ')
        math = input('Grade Math: ')
        science = input('Grade Science: ')
        english = input('Grade English: ')

        stud = Grades(filipino, math, science, english)
        stud.id = id
        stud.lastname = lastname
        stud.firstname = firstname
        stud.middlename = middlename
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        students.append(stud)
        ans = input('Enter another?[y/n]: ')

        if (ans != 'Y'):
            break
    menu()


def addTeachers():
    while True:
        print()
        print('Enter teacher information')
        id = input('Enter ID: ')
        lastname = input('Enter Last_name: ')
        firstname = input('Enter First_name: ')
        middlename = input('Enter Middle_name: ')
        type = input('Enter type: ')
        department = input('Enter Department: ')
        position = input('Enter Position: ')

        teach = Teacher(id, lastname, firstname, middlename, type, department, position)
        teach.id = id
        teach.lastname = lastname
        teach.firstname = firstname
        teach.middlename = middlename
        teach.type = type
        teach.department = department
        teach.position = position

        teachers.append(teach)
        ans = input('Enter another?[y/n]: ')

        if (ans != 'Y'):
            break

    menu()


def displayAll():
    print()
    print('--------------------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i}\t | {s.getName()}\t | {s.getCourse()}\t | {s.getAverage()}')
        i += 1
    for t in teachers:
        print(f'{i}\t | {t.getName()}\t | {t.getDept()}\t | {t.getPosition()}')
        i += 1
    print('--------------------------------------------------------------------------------------------')

    menu()


def deleteAll():
    students.clear()
    teachers.clear()

    print('ALL RECORDS HAS BEEN DELETED!')
    menu()


def deleteStudent():
    i = int(input('Enter index: '))
    students.pop(i)

    menu()


def deleteTeacher():
    i = int(input('Enter index: '))
    teachers.pop(i)

    menu()


def searchStudent():
    i = int(input('Enter index: '))
    print(f'{i}\t{students[i].getName()}\t | {students[i].getCourse()}\t | {students[i].getAverage()}')

    menu()


def searchTeacher():
    i = int(input('Enter index: '))
    print(f'{i}\t {teachers[i].getName()}\t |  {teachers[i].getDept()}\t | {teachers[i].getPosition()}')

    menu()


def displayStudent():
    print()
    print('-------------------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i}\t | {s.getName()}\t | {s.getCourse()}\t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------------------')
    menu()


def displayTeacher():
    print()
    print('-------------------------------------------------------------------------------------------')
    i = 0
    for t in teachers:
        toPrint = f'{i}\t | {t.getName()} | {t.getDept()}\t | {t.getPosition()}'
        print(toPrint)
        i += 1
    print('-------------------------------------------------------------------------------------------')
    menu()


def menu():
    print()
    print('::Menu::')
    print('D - delete student      S - search student')
    print('P - add  student        M -display student ')
    print('A - add  teacher        Z -display teacher ')
    print('G - delete teacher      C - search teacher ')
    print('X - delete all          Y - display all ')
    print()
    sss = input('Enter a function: ')
    choice = sss.upper()

    if choice == 'D':
        deleteStudent()
    elif choice == 'G':
        deleteTeacher()
    elif choice == 'P':
        addStudents()
    elif choice == 'A':
        addTeachers()
    elif choice == 'S':
        searchStudent()
    elif choice == 'C':
        searchTeacher()
    elif choice == 'M':
        displayStudent()
    elif choice == 'Z':
        displayTeacher()
    elif choice == 'Y':
        displayAll()
    elif choice == 'X':
        deleteAll()
    print()


menu()
