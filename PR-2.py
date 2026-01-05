student = ["Aditya", "Tanesh", "Ravi", "Sumanth"]
subjets = ["Maths", "Science", "English"]
marks = [[85, 92, 78], [88, 76, 90], [90, 91, 85], [70, 80, 75]]

total_students = len(student)
total_subjects = len(subjets)

def mean_marks(marks):
    mean_marks = []
    for i in range(total_subjects):
        subject_total = sum(marks[j][i] for j in range(total_students))
        mean_marks.append(subject_total / total_students)
    return mean_marks