students = [
    {"name": "Ana", "grades": [7, 9, 8]},
    {"name": "Luis", "grades": [5, 6, 4]},
    {"name": "Marta", "grades": [10, 9, 9]},
]

averages = {}

for student in students:
    nombre = student["name"]
    notas = student["grades"]

    media = sum(notas) / len(notas)

    averages[nombre] = round(media, 2)

    print(f"Alumno: {nombre} | Nota media: {media:.2f}")

best_student = None
best_average = -1

for student in students:
    nombre = student["name"]
    notas = student["grades"]
    media = sum(notas)

    if media > best_average:
        best_average = media
        best_student = nombre

print(f"El alumno con la mejor media es: {best_student}")