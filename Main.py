student_name = input("Please enter your full name: ")
age_input = input("Please enter your age: ")

if age_input.isdigit():
    student_age = int(age_input)
else:
    age_input_retry = input("Invalid input! Please enter digits only for age: ")
    if age_input_retry.isdigit():
        student_age = int(age_input_retry)
    else:
        print("Still invalid. Exiting.")
        exit()
if student_age < 18:
    print("Name:", student_name)
    print("Age:", student_age)
    print("You are a Primary School student.")
else:
    print("Name:", student_name)
    print("Age:", student_age)
    print("You are a College student.")


grade_for_current_year = input ("Please enter your grade for the current year")
if grade_for_current_year.isdigit():
    grade_for_current_year = int(grade_for_current_year)
else:
    print("Invalid input")
    grade_for_current_year_retry = input("Please enter digits only for grade: ")
    if grade_for_current_year_retry.isdigit():
        grade_for_current_year = int(grade_for_current_year_retry)
    else:
        print("Still invalid grade.")
        exit()

grade_for_past_year = input ("Please enter your grade for the past year")
if grade_for_past_year.isdigit():
    grade_for_past_year = int(grade_for_past_year)
else:
    print("Invalid input!")
    grade_for_past_year_retry = input("Please enter digits only for grade: ")
    if grade_for_past_year_retry.isdigit():
        grade_for_past_year = int(grade_for_past_year_retry)

average_grade = (grade_for_current_year + grade_for_past_year) /2
print ("Average Grade:", average_grade)
if average_grade <50:
    print ("Sorry, you are a loser, you need to have at least 50 grades.")
else:
    print ("Well done! You have enough grades.")

