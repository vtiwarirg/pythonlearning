# If you have a local file named caesar_art.py with a logo variable, import it directly
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for student, score in student_scores.items():
    if score >= 90:
        student_grades[student] = 'Outstanding'
    elif score >= 80:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
        
print("Student Grades:")
for student, grade in student_grades.items():
    print(f"{student}: {grade}")
        
        