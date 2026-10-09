students = [
    {"name": "Ana", "grades": [7, 9, 8]},
    {"name": "Luis", "grades": [5, 6, 4]},
    {"name": "Marta", "grades": [10, 9, 9]},
    {"name": "Pablo", "grades": [10, 10]},
    {"name": "Eva", "grades": [3, 4, 2]},
]

names = [student["name"] for student in students] # Nombre en student y los mete en una lista

averages = {student["name"]: sum(student["grades"]) / len(student["grades"]) for student in students} # Diccionario que empareja nombre con su nota media

approved = [name for name, average in averages.items() if average >= 5] # Solo nombre si su media es > o igual a 5

# Quiero el nombre... de cada nombre y media que encuentres en las medias... siempre y cuando la media sea mayor o igual a 5.


best_student = max(averages, key=averages.get)

has_a_ten = [student["name"] for student in students if 10 in student["grades"]]

print(names)
print(averages)
print(approved)
print(best_student)
print(has_a_ten)