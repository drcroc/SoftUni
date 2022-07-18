
command = ""
courses = {}
user_list = 'name'

while command != 'end':

    command = input()

    if command == 'end':
        break

    course_name, student_name = command.split(' : ')
    courses[course_name] = courses.get(course_name, [])
    courses[course_name].append(student_name)

for course_name in courses:
    print(f"{course_name}: {len(courses[course_name])}")
    for names in courses[course_name]:
        print(f'-- {names}')

