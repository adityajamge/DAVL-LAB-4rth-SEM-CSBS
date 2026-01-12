import pandas as pd

titanic = pd.read_csv('tested.csv')

print(titanic)
# print(titanic.head())   
# print(titanic.shape)
# print(titanic.columns)
# print(titanic.dtypes)
# print(titanic.describe())
# print(titanic.isnull().sum())
# print(titanic.nunique())
# print(titanic.corr())
# print(titanic.plot(kind='scatter', x='Age', y='Fare'))
# print(titanic.boxplot(column='Age'))
# print(titanic.hist(column='Age'))

# adity@INBOOK_Y2_PLUS MINGW64 /d/College/6th Sem/DAVL/PR-4 (main)
# $ C:/Users/adity/AppData/Local/Programs/Python/Python310/python.exe "d:/College/6th Sem/DAVL/PR-4/PR.py"
#      PassengerId  Survived  Pclass  ...      Fare Cabin  Embarked
# 0            892         0       3  ...    7.8292   NaN         Q
# 1            893         1       3  ...    7.0000   NaN         S
# 2            894         0       2  ...    9.6875   NaN         Q
# 3            895         0       3  ...    8.6625   NaN         S
# 4            896         1       3  ...   12.2875   NaN         S
# ..           ...       ...     ...  ...       ...   ...       ...
# 413         1305         0       3  ...    8.0500   NaN         S
# 414         1306         1       1  ...  108.9000  C105         C
# 415         1307         0       3  ...    7.2500   NaN         S
# 416         1308         0       3  ...    8.0500   NaN         S
# 417         1309         0       3  ...   22.3583   NaN         C

# can you use matplot lib in this tested.csv file? 

import matplotlib.pyplot as plt

# titanic.plot(kind='scatter', x='Age', y='Fare')
titanic.boxplot(column='Age')
titanic.hist(column='Age')
plt.show() 



# iris.csv file
# [418 rows x 12 columns]
#      sepal_length  sepal_width  petal_length  petal_width    species
# 0             5.1          3.5           1.4          0.2     setosa
# 1             4.9          3.0           1.4          0.2     setosa
# 2             4.7          3.2           1.3          0.2     setosa
# 3             4.6          3.1           1.5          0.2     setosa
# 4             5.0          3.6           1.4          0.2     setosa
# ..            ...          ...           ...          ...        ...
# 145           6.7          3.0           5.2          2.3  virginica
# 146           6.3          2.5           5.0          1.9  virginica
# 147           6.5          3.0           5.2          2.0  virginica
# 148           6.2          3.4           5.4          2.3  virginica
# 149           5.9          3.0           5.1          1.8  virginica

# [150 rows x 5 columns]


# ploting the iris.csv file 
iris = pd.read_csv('iris.csv')

iris.plot(kind='scatter', x='sepal_length', y='sepal_width')
iris.boxplot(column=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
iris.hist()
plt.show()


# use seaborn to plot the titanic.csv file 

import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.plot(kind='scatter', x='age', y='fare')
titanic.boxplot(column='age')
titanic.hist(column='age')
plt.show()



# errpr for gender
# Traceback (most recent call last):
#   File "C:\Users\adity\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
#     return self._engine.get_loc(casted_key)
#   File "pandas/_libs/index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
#   File "pandas/_libs/index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
#   File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item      
#   File "pandas/_libs/hashtable_class_helper.pxi", line 7096, in pandas._libs.hashtable.PyObjectHashTable.get_item      
# KeyError: 'Gender'

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "d:\College\6th Sem\DAVL\PR-4\PR.py", line 83, in <module>
#     titanic['Gender'].value_counts().plot(kind='bar')
#   File "C:\Users\adity\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\frame.py", line 4113, in __getitem__
#     indexer = self.columns.get_loc(key)
#   File "C:\Users\adity\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\indexes\base.py", line 3819, in get_loc
#     raise KeyError(key) from err
# KeyError: 'Gender' 


# also show gender distribution in titanic.csv file 
