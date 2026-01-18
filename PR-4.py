# Name: Aditya Babanrao Jamge
# PRN Number: RBTL25CB076

import math

print("Name: Aditya Babanrao Jamge")
print("PRN Number: RBTL25CB076")
print()

# =====================================================
# SCHOOL STUDENT MARKS ANALYSIS SYSTEM
# =====================================================

# =====================================================
# 1. STORE STUDENT NAMES AND MARKS USING VARIABLES, LISTS, AND TUPLES
# =====================================================

# Using variables for subjects
subject1 = "Mathematics"
subject2 = "Science"
subject3 = "English"
subject4 = "History"
subject5 = "Computer"

# Using tuple for subjects (immutable)
subjects = (subject1, subject2, subject3, subject4, subject5)

# Using list for student names
students = []

# Using list of tuples for storing marks (student_name, marks_tuple)
student_marks = []

# Input student data
print("=" * 60)
print("        STUDENT MARKS ENTRY SYSTEM")
print("=" * 60)

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    print(f"\n--- Student {i + 1} ---")
    name = input("Enter student name: ").strip()
    students.append(name)
    
    marks = []
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"  Enter marks in {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("  Please enter marks between 0 and 100.")
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
    
    # Store as tuple (immutable marks record)
    student_marks.append((name, tuple(marks)))

print("\n" + "=" * 60)
print("        STORED DATA DISPLAY")
print("=" * 60)

print(f"\nSubjects (Tuple): {subjects}")
print(f"Students (List): {students}")
print("\nStudent Marks (List of Tuples):")
for record in student_marks:
    print(f"  {record[0]}: {record[1]}")

# =====================================================
# 2. CALCULATE TOTAL, AVERAGE, AND PERCENTAGE FOR EACH STUDENT
# =====================================================

print("\n" + "=" * 60)
print("        TOTAL, AVERAGE, AND PERCENTAGE")
print("=" * 60)

student_results = []  # Store results for later use

for name, marks in student_marks:
    total = sum(marks)
    average = total / len(marks)
    percentage = (total / (len(marks) * 100)) * 100
    
    student_results.append({
        'name': name,
        'marks': marks,
        'total': total,
        'average': average,
        'percentage': percentage
    })
    
    print(f"\n{name}:")
    print(f"  Marks: {marks}")
    print(f"  Total: {total:.2f}")
    print(f"  Average: {average:.2f}")
    print(f"  Percentage: {percentage:.2f}%")

# =====================================================
# 3. DETERMINE PASS/FAIL STATUS AND ASSIGN GRADES
# =====================================================

print("\n" + "=" * 60)
print("        PASS/FAIL STATUS AND GRADES")
print("=" * 60)

def get_grade(percentage):
    """Assign grade based on percentage"""
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "F"

def get_status(percentage):
    """Determine pass/fail status"""
    return "PASS" if percentage >= 40 else "FAIL"

print(f"\n{'Student':<20} {'Percentage':<12} {'Grade':<8} {'Status'}")
print("-" * 50)

for result in student_results:
    grade = get_grade(result['percentage'])
    status = get_status(result['percentage'])
    result['grade'] = grade
    result['status'] = status
    print(f"{result['name']:<20} {result['percentage']:<12.2f} {grade:<8} {status}")

# =====================================================
# 4. IDENTIFY HIGHEST/LOWEST MARKS AND PRINT EVEN MARKS
# =====================================================

print("\n" + "=" * 60)
print("        HIGHEST AND LOWEST MARKS ANALYSIS")
print("=" * 60)

# Find student with highest and lowest total marks
highest_student = max(student_results, key=lambda x: x['total'])
lowest_student = min(student_results, key=lambda x: x['total'])

print(f"\nStudent with Highest Total Marks:")
print(f"  {highest_student['name']} with {highest_student['total']:.2f} marks")

print(f"\nStudent with Lowest Total Marks:")
print(f"  {lowest_student['name']} with {lowest_student['total']:.2f} marks")

# Highest and lowest in each subject
print("\nSubject-wise Highest and Lowest:")
for i, subject in enumerate(subjects):
    subject_marks_list = [(result['name'], result['marks'][i]) for result in student_results]
    highest = max(subject_marks_list, key=lambda x: x[1])
    lowest = min(subject_marks_list, key=lambda x: x[1])
    print(f"\n  {subject}:")
    print(f"    Highest: {highest[0]} ({highest[1]:.2f})")
    print(f"    Lowest: {lowest[0]} ({lowest[1]:.2f})")

# Print all even marks
print("\n" + "=" * 60)
print("        ALL EVEN MARKS")
print("=" * 60)

all_marks = []
for result in student_results:
    all_marks.extend(result['marks'])

even_marks = [int(mark) for mark in all_marks if int(mark) % 2 == 0]
print(f"\nAll marks: {[int(m) for m in all_marks]}")
print(f"Even marks: {even_marks}")

# =====================================================
# 5. RESULT ANALYSIS - MEAN, MEDIAN, MODE, STANDARD DEVIATION
# =====================================================

print("\n" + "=" * 60)
print("        RESULT ANALYSIS (STATISTICAL MEASURES)")
print("=" * 60)

# Statistical functions
def mean(ar):
    """Calculate mean of a list"""
    return sum(ar) / len(ar)

def median(ar):
    """Calculate median of a list"""
    sorted_ar = sorted(ar)
    n = len(sorted_ar)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_ar[mid - 1] + sorted_ar[mid]) / 2
    else:
        return sorted_ar[mid]

def mode(ar):
    """Calculate mode of a list"""
    frequency = {}
    for i in ar:
        frequency[i] = frequency.get(i, 0) + 1
    
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    
    if len(modes) == len(frequency):
        return "No mode (all values unique)"
    return modes

def variance(ar):
    """Calculate variance of a list"""
    m = mean(ar)
    return sum((x - m) ** 2 for x in ar) / len(ar)

def std_dev(ar):
    """Calculate standard deviation of a list"""
    return math.sqrt(variance(ar))

# Calculate statistics for each subject (course)
print("\nStatistical Analysis for Each Subject/Course:")
print("-" * 60)

for i, subject in enumerate(subjects):
    subject_marks_list = [result['marks'][i] for result in student_results]
    
    print(f"\n{subject}:")
    print(f"  All Marks: {subject_marks_list}")
    print(f"  Mean: {mean(subject_marks_list):.2f}")
    print(f"  Median: {median(subject_marks_list):.2f}")
    print(f"  Mode: {mode(subject_marks_list)}")
    print(f"  Standard Deviation: {std_dev(subject_marks_list):.2f}")
    print(f"  Variance: {variance(subject_marks_list):.2f}")

# Overall statistics
print("\n" + "=" * 60)
print("        OVERALL CLASS STATISTICS")
print("=" * 60)

all_percentages = [result['percentage'] for result in student_results]
all_totals = [result['total'] for result in student_results]

print(f"\nClass Average Percentage: {mean(all_percentages):.2f}%")
print(f"Median Percentage: {median(all_percentages):.2f}%")
print(f"Standard Deviation of Percentages: {std_dev(all_percentages):.2f}")

# Grade distribution
print("\nGrade Distribution:")
grade_counts = {"A": 0, "B": 0, "C": 0, "F": 0}
for result in student_results:
    grade_counts[result['grade']] += 1

for grade, count in grade_counts.items():
    if count > 0:
        bar = "#" * count
        percentage = (count / len(student_results)) * 100
        print(f"  Grade {grade}: {bar} ({count} student(s) - {percentage:.1f}%)")

# Pass/Fail summary
pass_count = sum(1 for r in student_results if r['status'] == "PASS")
fail_count = len(student_results) - pass_count

print(f"\nPass/Fail Summary:")
print(f"  Passed: {pass_count} student(s)")
print(f"  Failed: {fail_count} student(s)")
print(f"  Pass Rate: {(pass_count / len(student_results)) * 100:.2f}%")

print("\n" + "=" * 60)
print("        ANALYSIS COMPLETE!")
print("=" * 60)