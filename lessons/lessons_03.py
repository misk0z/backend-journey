def calculate_average(grades: list[int]) -> float:
    #Suma todas las notas de la lista y las divide entre cuántas hay para sacar la media
    return sum(grades) / len(grades)

def build_averages(students: list[dict]) -> dict[str, float]:
    #Recorre cada alumno, cogemos nombre como clave y calcula la media usando al función calculate_average
    return {
        student["name"]: calculate_average(student["grades"]) 
        for student in students
        }

def get_approved(averages: dict[str, float], minimum: float = 5.0   ) -> list[str]:
    #Filtra y devuelve nombre con la media igual o superior al minimo
    return [name for name, average in averages.items() if average >= minimum]

def get_best_student(averages: dict[str, float]) -> str:
    #Busca y devuelve la clave(nombre) que tenga el valor númerico(nota) más alto
    return max(averages, key=averages.get)

def main() -> None:
    """"Run the main program logic."""
    students = [
    {"name": "Ana", "grades": [7, 9, 8]},
    {"name": "Luis", "grades": [5, 6, 4]},
    {"name": "Marta", "grades": [10, 9, 9]},
    {"name": "Pablo", "grades": [10, 10]},
    {"name": "Eva", "grades": [3, 4, 2]},
]

    averages = build_averages(students)

    approved = get_approved(averages)

    best = get_best_student(averages)

    print("Averages: ", averages)
    print("Approved: ", approved)
    print("Best student: ", best)

if __name__ == "__main__":
    main()