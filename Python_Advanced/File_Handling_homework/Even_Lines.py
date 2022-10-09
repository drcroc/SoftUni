
replacement_symbols = ["-", ",", ".", "!", "?"]
with open('./test_files/Input_exercise_1.TXT') as file:
    odd_line = 1
    for line in file:
        if not odd_line % 2 == 0:
            for char in line:
                if char in replacement_symbols:
                    line = line.replace(char, '@')

            current_line = line.split()
            print(*current_line[::-1])

        odd_line += 1









