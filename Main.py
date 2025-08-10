student_name = input ("Please enter your full name.")
student_age = int(input ("please enter your age"))
if student_age <18:
    print ("Name:",student_name)
    print ("Age",student_age)
    print ("You are a Primary School student")
else:
    print ("Name:",student_name)
    print ("Age",student_age)
    print ("You are a College student")

grade_for_current_year = int(input ("Please enter your grade for_the_current_year"))
grade_for_past_year = int(input ("Please enter your grade for_past_year"))
total_grade = (grade_for_current_year + grade_for_past_year) /2
print ("Total Grade:", total_grade)
if total_grade <50:
    print ("Sorry, you are a loser")
else:
    print ("Well done!")
    print ("bye!")
