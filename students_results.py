import random

grades = [[random.randint(0, 100) for _ in range(3)] for _ in range(100)]

for i, student_grades in enumerate(grades):
    average_score = sum(student_grades) / len(student_grades)
    print(f"Студент {i+1}: Оцінки = {student_grades}, Середній бал = {average_score:.2f}")
