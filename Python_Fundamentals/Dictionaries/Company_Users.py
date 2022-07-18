# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
#     • Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
#     • The input always will be valid.


companies = {}
while True:
    command = input()
    if command == 'End':
        break
    company_name, personal_id = command.split(' -> ')

    if company_name in companies:
        if personal_id in companies[company_name]:
            continue

    companies[company_name] = companies.get(company_name, [])
    companies[company_name].append(personal_id)

for names in companies:
    print(names)
    for ids in companies[names]:
        print(f'-- {ids}')























