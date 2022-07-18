
student_count = int(input())
student_class = {}


for i in range(student_count):
    name = str(input())
    student_class[name] = student_class.get(name, [])
    grade = float(input())
    student_class[name].append(grade)


for students in student_class:
    averageGrade = sum(student_class[students])/len(student_class[students])
    if averageGrade >= 4.50:
        print(f'{students} -> {averageGrade:.2f}')
