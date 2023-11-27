# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #removed one parenthesis on the right that was unnecessary
#added int value for clarification, since you seem to want to input only numbers (funnily enough, this means I have to add the parenthesis back)             
# changed by: UserLAZ (LA886@live.mdx.ac.uk)

exam_3 = int(input("Input exam grade three: "))# str can't add numbers as value. It should be int based on previous functions
# changed by UserLAZ (LA886@mdx.ac.uk)

grades = [exam_one, exam_two, exam_3] #need to put commas (,) to seperate the different functions in the list
# "exam_three is not defined. The user was likely thinking of exam_3
#changed by UserLAZ (LA886@live.mdx.ac.uk)
summ = 0 # should use a different name than "sum", as to not confuse the program.
# changed by UserLAZ (LA886@live.mdx.ac.uk)
for grade in grades: # You likely meant to say "for grade in grades". You don't have an existing value for grade.
  #changed by UserLAZ (LA886@live.mdx.ac.uk)
  summ = summ + grade

avg = summ / len(grades) # grdes is a typo of grades
# changed by UserLAZ (LA886@live.mdx.ac.uk)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #forgot to add :
#changed by UserLAZ (LA886@live.mdx.ac.uk)
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C" # "C' should be written as "C" instead.
  # changed by UserLAZ (LA886@live.mdx.ac.uk)
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
    # for the last "if" alternatives, you should write "else" instead of another "elif"
    # changed by UserLAZ (LA886@live.mdx.ac.uk)
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))# grade and avg are not strings, they're numbers
    # changed by UserLAZ (LA886@live.mdx.ac.uk)

    print("Average: " + str(avg))

    print("Grade: " + str(letter_grade))

# "letter_grade" is misswritten as "letter-grade"
# changed by UserLAZ (LA886@live.mdx.ac.uk)
if letter_grade is "F":
  # need to put the text inside parenthesis ()
  # changed by UserLAZ (LA886@live.mdx.ac.uk)
    print ("Student is failing.")
else:
    print ("Student is passing.")
