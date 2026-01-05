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
