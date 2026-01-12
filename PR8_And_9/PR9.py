import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

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

print("Name: Aditya Babanrao Jamge")
print("RBTL25CB076")

print("=" * 60)
print("           IRIS DATASET ANALYSIS")
print("=" * 60)

iris = pd.read_csv('iris.csv')
print(iris)

print("\n\nHead of the iris data :")
print(iris.head())

print("\n\nTail of the iris data :")
print(iris.tail())

print("\n\nShape of the iris data :")
print(iris.shape)

print("\n\nColumns of the iris data :")
print(iris.columns)

print("\n\nInfo of the iris data :")
print(iris.info())

print("\n\nDescribe of the iris data :")
print(iris.describe())

print("\n\nMissing Values of the iris data :")
print(iris.isnull().sum())

print("\n\nDuplicate Values of the iris data :")
print(iris.duplicated().sum())

print("\n\nValue count by species :")
print(iris['species'].value_counts())

numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

print("\n" + "=" * 60)
print("    STATISTICAL ANALYSIS (Custom Functions)")
print("=" * 60)

for col in numeric_columns:
    data = iris[col].dropna().tolist()
    print(f"\n{col}:")
    print(f"  Mean: {mean(data):.4f}")
    print(f"  Median: {median(data):.4f}")
    print(f"  Mode: {mode(data)}")
    print(f"  Variance: {variance(data):.4f}")
    print(f"  Std Dev: {std_dev(data):.4f}")

print("\n" + "=" * 60)
print("    COVARIANCE & CORRELATION MATRIX")
print("=" * 60)

print("\nCovariance (Custom Function):")
for i, col1 in enumerate(numeric_columns):
    for j, col2 in enumerate(numeric_columns):
        if i < j:
            data1 = iris[col1].dropna().tolist()
            data2 = iris[col2].dropna().tolist()
            print(f"  {col1} & {col2}: {covariance(data1, data2):.4f}")

print("\nCorrelation (Custom Function):")
for i, col1 in enumerate(numeric_columns):
    for j, col2 in enumerate(numeric_columns):
        if i < j:
            data1 = iris[col1].dropna().tolist()
            data2 = iris[col2].dropna().tolist()
            print(f"  {col1} & {col2}: {correlation(data1, data2):.4f}")

print("\n" + "=" * 60)
print("    SPECIES-WISE STATISTICS")
print("=" * 60)

for species in iris['species'].unique():
    species_data = iris[iris['species'] == species]
    print(f"\n{species.upper()}:")
    for col in numeric_columns:
        data = species_data[col].dropna().tolist()
        print(f"  {col}:")
        print(f"    Mean: {mean(data):.4f}, Std Dev: {std_dev(data):.4f}")

print("\n\nOperations using numpy :")
for col in numeric_columns:
    print(f"\n{col}:")
    print(f"  Mean (numpy): {np.mean(iris[col]):.4f}")
    print(f"  Median (numpy): {np.median(iris[col]):.4f}")
    print(f"  Std Dev (numpy): {np.std(iris[col]):.4f}")

print("\n\nVisualizations using seaborn :")

plt.figure(figsize=(12, 8))
plt.suptitle('Iris Dataset Visualizations')

plt.subplot(2, 2, 1)
sns.boxplot(data=iris[numeric_columns])
plt.title('Boxplot of All Features')

plt.subplot(2, 2, 2)
sns.histplot(data=iris, x='sepal_length', hue='species', kde=True)
plt.title('Sepal Length Distribution')

plt.subplot(2, 2, 3)
sns.histplot(data=iris, x='petal_length', hue='species', kde=True)
plt.title('Petal Length Distribution')

plt.subplot(2, 2, 4)
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.title('Sepal Length vs Width')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.pairplot(iris, hue='species')
plt.show()

print("\n" + "=" * 60)
print("           Analysis Complete!")
print("=" * 60)
