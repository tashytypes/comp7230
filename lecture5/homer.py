# TODO: write code to open file 'first_names.txt' as file_1
file_1 = open("academics.txt", "r")
# TODO: write code to open file 'last_names.txt' as file_2
file_2 = open("foo.txt", "r")
for (line_1, line_2) in zip(file_1, file_2):
    print(line_1.strip() + " " + line_2.strip())

file_1.close()
file_2.close()