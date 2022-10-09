import os

extensions = {}

path = input()
#               /for current folder + sub folders\
# #########################################################
directory = os.walk(path)
for direct in directory:
    for files in direct[-1]:
        file_name, extension = files.split('.')
        if extension not in extensions.keys():
            extensions[extension] = []

        extensions[extension].append(file_name)
# #########################################################


#                    \for the current folder/
# #########################################################
# directory = os.listdir(path)
# for files in directory:
#     if os.path.isfile(files):
#         file_name, extension = files.split('.')
#         if extension not in extensions.keys():
#             extensions[extension] = []
#
#         extensions[extension].append(file_name)
# #########################################################

with open(f"./test_files/report.txt", "w") as f:
    for extension in sorted(extensions.keys()):
        # print(f'.{extension}')
        f.write(f'.{extension}\n')
        for files in sorted(extensions[extension]):
            # print(f'- - - {files}.{extension}')
            f.write(f'- - - {files}.{extension}\n')

with open(f"./report.txt", "w") as f:
    for extension in sorted(extensions.keys()):
        f.write(f'.{extension}\n')
        for files in sorted(extensions[extension]):
            f.write(f'- - - {files}.{extension}\n')

