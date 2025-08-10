
while True:
    max_input = input("Enter the maximum number of students: ")
    if max_input.isdigit():
        max_students = int(max_input)
        break
    print(" Please enter a positive number.")

students = []

while len(students) < max_students:

    add_student = input("Do you want to add a student? (yes/no): ")
    if add_student != "yes":
        print("Please enter a valid input.")
        break

    student_name = input("Enter student name: ")
    age_in = input("Enter age: ")
    if age_in.isdigit():
        student_age = int(age_in)
    else:
        retry = input("Invalid age! Digits only: ")
        if retry.isdigit():
            student_age = int(retry)
        else:
            print("Still invalid. Skipping this student.")
            continue

    students.append({
        "name":   student_name,
        "age":    student_age,

    })

    if len(students) == max_students:
        print(f"\n Reached the maximum of {max_students} students.\n")

print("\n--- All Students ---")
for s in students:
    print("Name:",   s["name"])
    print("Age:",    s["age"])
