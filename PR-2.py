import math

def get_student_data():
    students = []
    subjects = []
    marks = []
    
    while True:
        try:
            num_subjects = int(input("Enter the number of subjects: "))
            if num_subjects > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print(f"\nEnter the names of {num_subjects} subjects:")
    for i in range(num_subjects):
        subject = input(f"  Subject {i + 1}: ").strip()
        subjects.append(subject)
    
    while True:
        try:
            num_students = int(input("\nEnter the number of students: "))
            if num_students > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print(f"\nEnter details for {num_students} students:")
    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")
        name = input("  Name: ").strip()
        students.append(name)
        
        student_marks = []
        for j, subject in enumerate(subjects):
            while True:
                try:
                    mark = float(input(f"  {subject} marks (0-100): "))
                    if 0 <= mark <= 100:
                        student_marks.append(mark)
                        break
                    print("  Please enter marks between 0 and 100.")
                except ValueError:
                    print("  Invalid input. Please enter a valid number.")
        marks.append(student_marks)
    
    return students, subjects, marks

def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def get_grade_description(grade):
    descriptions = {
        "A+": "Outstanding",
        "A": "Excellent",
        "B+": "Very Good",
        "B": "Good",
        "C": "Average",
        "D": "Below Average",
        "F": "Fail"
    }
    return descriptions.get(grade, "Unknown")

print("=" * 60)
print("        STUDENT MARKS ANALYSIS SYSTEM")
print("=" * 60)
student, subjets, marks = get_student_data()
total_students = len(student)
total_subjects = len(subjets)

def mean(ar):
    return sum(ar) / len(ar)

def median(ar):
    sorted_ar = sorted(ar)
    n = len(sorted_ar)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_ar[mid - 1] + sorted_ar[mid]) / 2
    else:
        return sorted_ar[mid]

def mode(ar):
    frequency = {}
    for i in ar:
        frequency[i] = frequency.get(i, 0) + 1
    
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    
    if len(modes) == len(frequency):
        return None
    return modes

def variance(ar):
    m = mean(ar)
    return sum((x - m) ** 2 for x in ar) / len(ar)

def std_dev(ar):
    return math.sqrt(variance(ar))

def covariance(ar1, ar2):
    mean1 = mean(ar1)
    mean2 = mean(ar2)
    
    covar = sum((ar1[i] - mean1) * (ar2[i] - mean2) for i in range(len(ar1))) / len(ar1)
    return covar

def correlation(ar1, ar2):
    covar = covariance(ar1, ar2)
    stddev1 = std_dev(ar1)
    stddev2 = std_dev(ar2)
    
    return covar / (stddev1 * stddev2)

def mean_marks(marks):
    mean_marks = []
    for i in range(total_subjects):
        subject_total = sum(marks[j][i] for j in range(total_students))
        mean_marks.append(subject_total / total_students)
    return mean_marks

def median_marks(marks):
    median_marks = []
    for i in range(total_subjects):
        subject_marks = [marks[j][i] for j in range(total_students)]
        median_marks.append(median(subject_marks))
    return median_marks

def mode_marks(marks):
    mode_marks = []
    for i in range(total_subjects):
        subject_marks = [marks[j][i] for j in range(total_students)]
        mode_marks.append(mode(subject_marks))
    return mode_marks

def variance_marks(marks):
    variance_marks = []
    for i in range(total_subjects):
        subject_marks = [marks[j][i] for j in range(total_students)]
        variance_marks.append(variance(subject_marks))
    return variance_marks

def std_dev_marks(marks):
    std_dev_marks = []
    for i in range(total_subjects):
        subject_marks = [marks[j][i] for j in range(total_students)]
        std_dev_marks.append(std_dev(subject_marks))
    return std_dev_marks

print("=" * 60)
print(f"{'Students':<15} {', '.join(student)}")
print(f"{'Subjects':<15} {', '.join(subjets)}")
print("=" * 60)

print("\nMean Marks per Subject:")
mean_values = mean_marks(marks)
for i, subject in enumerate(subjets):
    print(f"  {subject}: {mean_values[i]:.2f}")

print("\nMedian Marks per Subject:")
median_values = median_marks(marks)
for i, subject in enumerate(subjets):
    print(f"  {subject}: {median_values[i]:.2f}")

print("\nMode Marks per Subject:")
mode_values = mode_marks(marks)
for i, subject in enumerate(subjets):
    print(f"  {subject}: {mode_values[i]}")

print("\nVariance of Marks per Subject:")
variance_values = variance_marks(marks)

for i, subject in enumerate(subjets):
    print(f"  {subject}: {variance_values[i]:.2f}")

print("\nStandard Deviation of Marks per Subject:")
std_dev_values = std_dev_marks(marks)
for i, subject in enumerate(subjets):
    print(f"  {subject}: {std_dev_values[i]:.2f}")

print("\n" + "=" * 60)
print("Student-wise Statistics with Grades:")
print("=" * 60)
for j, s_name in enumerate(student):
    student_marks = marks[j]
    avg = mean(student_marks)
    grade = get_grade(avg)
    description = get_grade_description(grade)
    print(f"\n{s_name}:")
    print(f"  Mean: {avg:.2f}")
    print(f"  Median: {median(student_marks):.2f}")
    print(f"  Mode: {mode(student_marks)}")
    print(f"  Variance: {variance(student_marks):.2f}")
    print(f"  Std Dev: {std_dev(student_marks):.2f}")
    print(f"  Total Marks: {sum(student_marks)}")
    print(f"  Grade: {grade} ({description})")

print("\n" + "=" * 60)
print("                 GRADE REPORT SUMMARY")
print("=" * 60)
print(f"{'Student':<20} {'Average':<10} {'Grade':<6} {'Status'}")
print("-" * 60)

for j, s_name in enumerate(student):
    avg = mean(marks[j])
    grade = get_grade(avg)
    description = get_grade_description(grade)
    print(f"{s_name:<20} {avg:<10.2f} {grade:<6} {description}")

print("-" * 60)

print("\nGrade Distribution:")
grade_counts = {"A+": 0, "A": 0, "B+": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for j in range(total_students):
    avg = mean(marks[j])
    grade = get_grade(avg)
    grade_counts[grade] += 1

for grade, count in grade_counts.items():
    if count > 0:
        percentage = (count / total_students) * 100
        bar = "█" * count
        print(f"  {grade}: {bar} ({count} student(s) - {percentage:.1f}%)")

print("\n" + "=" * 60)
print("           Analysis Complete!")
print("=" * 60)