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
print("           TITANIC DATASET ANALYSIS")
print("=" * 60)

titanic = pd.read_csv('tested.csv')
print(titanic)

print("\n\nHead of the titanic data :")
print(titanic.head())

print("\n\nTail of the titanic data :")
print(titanic.tail())

print("\n\nShape of the titanic data :")
print(titanic.shape)

print("\n\nColumns of the titanic data :")
print(titanic.columns)

print("\n\nInfo of the titanic data :")
print(titanic.info())

print("\n\nDescribe of the titanic data :")
print(titanic.describe())

print("\n\nMissing Values of the titanic data :")
print(titanic.isnull().sum())

print("\n\nDuplicate Values of the titanic data :")
print(titanic.duplicated('Age'))

print("\n\n Value count of the titanic data :")
print(titanic.value_counts())

print("\n\n Operations using numpy :")
print(np.mean(titanic['Age']))
print(np.median(titanic['Age']))
print(np.std(titanic['Age']))

print("\n\n Operations using seaborn :")
sns.boxplot(x='Age', data=titanic)
sns.histplot(x='Age', data=titanic)
plt.show()

print("\n\n Operations using seaborn :")
sns.countplot(x='Gender', data=titanic)
sns.boxplot(x='Gender', data=titanic)
sns.histplot(x='Gender', data=titanic)
plt.show()

print("\n" + "=" * 60)
print("           Analysis Complete!")
print("=" * 60)
