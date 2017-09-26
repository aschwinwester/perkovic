def avg(studentsGrades):
    for studentGrade in studentsGrades:
        avg = sum(studentGrade) / len(studentGrade)
        print(avg)

avg([[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]])