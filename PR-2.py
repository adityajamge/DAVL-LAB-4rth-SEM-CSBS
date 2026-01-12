import math

student = ["Aditya", "Tanesh", "Ravi", "Sumanth"]
subjets = ["Maths", "Science", "English"]
marks = [[85, 92, 78], [88, 76, 90], [90, 91, 85], [70, 80, 75]]
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

# Display Results
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
print("Student-wise Statistics:")
print("=" * 60)
for j, s_name in enumerate(student):
    student_marks = marks[j]
    print(f"\n{s_name}:")
    print(f"  Mean: {mean(student_marks):.2f}")
    print(f"  Median: {median(student_marks):.2f}")
    print(f"  Mode: {mode(student_marks)}")
    print(f"  Variance: {variance(student_marks):.2f}")
    print(f"  Std Dev: {std_dev(student_marks):.2f}")
    print(f"  Total Marks: {sum(student_marks)}")

print("\n" + "=" * 60)