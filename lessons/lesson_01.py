students = [
    {"name": "Ana", "grades": [7, 9, 8]},
    {"name": "Luis", "grades": [5, 6, 4]},
    {"name": "Marta", "grades": [10, 9, 9]},
    {"name": "Pablo", "grades": [10, 10]}
]

averages = {}

for student in students:
    name = student["name"]
    grades = student["grades"]

    average = sum(grades) / len(grades)

    averages[name] = average

    print(f"Alumno: {name} | Nota media: {average:.2f}")

best_student = None
best_average = -1

for name, average in averages.items():
    if average > best_average:
        best_average = average
        best_student = name

print(f"El alumno con la mejor media es: {best_student}")