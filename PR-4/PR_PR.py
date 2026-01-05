import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


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
