

project = []
students = []
teachers = []
labs = []

def add_teacher(name):
    t = [name]
    teachers.append(t)

def add_student(stdid, name):
    s = [stdid, name]
    students.append(s)

#students = [['90102234', 'hassan', 'ali'], ['9100033', 'ali', 'ahmad']]
#teachers = [['ali', 34], ['ahmad', 40]]

def get_teacher_age(stdid):
    student = 0
    for i in range(len(students)):
        s = students[i]
        if s[0] == stdid:
            student = s
            break
    if student == 0:
        return -1

    teacher_name = student[2]

    teacher = 0
    for i in range(len(teachers)):
        s = teachers[i]
        if s[0] == teacher_name:
            teacher = s
            break
    if teacher == 0:
        return -1

    return teacher[1]

#age = get_teacher_age(90102234)



s = input()
if s == 'add-student':
    n = int(input())
    for i in range(n):
        l = input()
        a = l.split(' ')
        add_student(int(a[0]), a[1])
elif s == 'add-teacher':
    pass
