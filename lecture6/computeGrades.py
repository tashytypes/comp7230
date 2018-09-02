import csv

def convert_to_letter_grade(grade):
    """Converts from a numerical grade to a letter grade."""
    if (grade >= 85.0):return "HD"
    elif (grade >= 75.0):return "D"
    elif (grade >= 65.0):return "CR"
    elif (grade >= 50.0):return "P"
    else: return "F"

#initialise list of final grades
final_grades = []

#read in student files and compute grades

fh = open("gradeees.csv", "r")
reader = csv.reader(fh)
next(reader) #skips first line

for row in reader:
    student_name = row[0]
    student_grade = 0.25 * sum([float(i) for i in row[1:]])
    letter_grade = convert_to_letter_grade(student_grade)
    final_grades.append([student_name, letter_grade])

fh.close()

# print (final_grades)

# write grades to a new file

fh = open("final_grades.csv", "w")
writer = csv.writer(fh)
for row in final_grades:
    writer.writerow(row)
fh.close()
