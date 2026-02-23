print("Class Attendance")
students = []
present = []

# Loop to collect student names
for i in range(3):
    name = input("Enter name: ")
    students.append(name)

# Loop to collect present students
for i in range(2):
    p = input("Enter present student: ")
    present.append(p)

# Logic to check attendance
for s in students:
    if s in present:
        print(s, "Present")
    else:
        print(s, "Absent")

print("Done")