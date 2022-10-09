import os

command = input()
while command != "End":
    try:
        command, file_name, *info = command.split('-')
        path = f"./test_files/{file_name}"

        try:
            # if os.path.exists(path):
            if command == 'Create':
                with open(path, 'w') as f:
                    f.close()

            elif command == 'Add':
                text = info[-1]
                with open(path, 'a') as f:
                    f.writelines(f'{text} \n')
                    f.close()

            elif command == 'Replace':
                old_string, new_string = info
                with open(path, 'r') as f:
                    text = f.read()
                    text = text.replace(old_string, new_string)
                with open(path, 'wt') as f:
                    f.write(text)

            elif command == 'Delete':
                os.remove(path)

        except FileNotFoundError:
            print(f"An error occurred")
            # print(f'The file "{file_name}" does not exist. Please enter valid file.')
    except ValueError:
        print(f"An error occurred")
        # print(f'Enter valid command.')
    command = input()
