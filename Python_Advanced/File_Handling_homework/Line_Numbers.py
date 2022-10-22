punctuation_marks = ["-", ",", ".", "!", "?", "'", '"']

with open('./test_files/Input_exercise_2.TXT') as file:
    line_index = 1
    for line in file:
        count_punctuation, letters_count = 0, 0
        for char in line:
            if char in punctuation_marks:
                count_punctuation += 1
            elif char.isalpha():
                letters_count += 1
        with open(f"./test_files/output.txt", "a") as f:
            f.write(f'Line {line_index}: {line.strip()} ({letters_count})({count_punctuation})\n')
        with open(f"./output.txt", "a") as f:
            f.write(f'Line {line_index}: {line.strip()} ({letters_count})({count_punctuation})\n')
        line_index += 1


