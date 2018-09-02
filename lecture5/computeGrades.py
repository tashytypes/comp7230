import csv

#initialise list of final grades
final_grades = []

#read in student files and compute grades

fh = open("gradeees.csv", "r")
reader = csv.reader(fh)
next(reader) #skips first line

for row in reader:
    student_name = row[0]
    student_grade = 0.25 * sum([float(i) for i in row[1:]])
    final_grades.append([student_name, student_grade])

fh.close()

# print (final_grades)

# write grades to a new file

fh = open("final_grades.csv", "w")
writer = csv.writer(fh)
for row in final_grades:
    writer.writerow(row)
fh.close()
