# Name: Aditya Babanrao Jamge
# PRN Number: RBTL25CB076

import math

print("Name: Aditya Babanrao Jamge")
print("PRN Number: RBTL25CB076")
print()

# =====================================================
# STATISTICAL MEASURES CALCULATOR
# =====================================================

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
        return "No mode (all values are unique)"
    return modes

def variance(ar):
    """Calculate variance of a list"""
    m = mean(ar)
    return sum((x - m) ** 2 for x in ar) / len(ar)

def std_dev(ar):
    """Calculate standard deviation of a list"""
    return math.sqrt(variance(ar))

def covariance(ar1, ar2):
    """Calculate covariance between two lists"""
    mean1 = mean(ar1)
    mean2 = mean(ar2)
    covar = sum((ar1[i] - mean1) * (ar2[i] - mean2) for i in range(len(ar1))) / len(ar1)
    return covar

def correlation(ar1, ar2):
    """Calculate correlation between two lists"""
    covar = covariance(ar1, ar2)
    stddev1 = std_dev(ar1)
    stddev2 = std_dev(ar2)
    return covar / (stddev1 * stddev2)

# =====================================================
# USER INPUT
# =====================================================

print("=" * 60)
print("        STATISTICAL MEASURES CALCULATOR")
print("=" * 60)

# Get first dataset from user
print("\n--- Enter First Dataset ---")
n1 = int(input("Enter the number of elements in first dataset: "))
data1 = []
print(f"Enter {n1} numbers:")
for i in range(n1):
    value = float(input(f"  Element {i + 1}: "))
    data1.append(value)

# Get second dataset from user (for covariance and correlation)
print("\n--- Enter Second Dataset (for Covariance and Correlation) ---")
print(f"Note: Must have same number of elements ({n1})")
data2 = []
print(f"Enter {n1} numbers:")
for i in range(n1):
    value = float(input(f"  Element {i + 1}: "))
    data2.append(value)

# =====================================================
# CALCULATE AND DISPLAY RESULTS
# =====================================================

print("\n" + "=" * 60)
print("        RESULTS FOR FIRST DATASET")
print("=" * 60)

print(f"\nData: {data1}")
print(f"\nMean: {mean(data1):.4f}")
print(f"Median: {median(data1):.4f}")
print(f"Mode: {mode(data1)}")
print(f"Variance: {variance(data1):.4f}")
print(f"Standard Deviation: {std_dev(data1):.4f}")

print("\n" + "=" * 60)
print("        RESULTS FOR SECOND DATASET")
print("=" * 60)

print(f"\nData: {data2}")
print(f"\nMean: {mean(data2):.4f}")
print(f"Median: {median(data2):.4f}")
print(f"Mode: {mode(data2)}")
print(f"Variance: {variance(data2):.4f}")
print(f"Standard Deviation: {std_dev(data2):.4f}")

print("\n" + "=" * 60)
print("        RELATIONSHIP BETWEEN DATASETS")
print("=" * 60)

cov = covariance(data1, data2)
corr = correlation(data1, data2)

print(f"\nCovariance: {cov:.4f}")
print(f"Correlation: {corr:.4f}")

# Interpret correlation
if corr > 0.7:
    interpretation = "Strong Positive Correlation"
elif corr > 0.4:
    interpretation = "Moderate Positive Correlation"
elif corr > 0:
    interpretation = "Weak Positive Correlation"
elif corr > -0.4:
    interpretation = "Weak Negative Correlation"
elif corr > -0.7:
    interpretation = "Moderate Negative Correlation"
else:
    interpretation = "Strong Negative Correlation"

print(f"Interpretation: {interpretation}")

print("\n" + "=" * 60)
print("        ANALYSIS COMPLETE!")
print("=" * 60)
