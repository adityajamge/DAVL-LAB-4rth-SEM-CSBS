# Name: Aditya Babanrao Jamge
# PRN Number: RBTL25CB076

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("Name: Aditya Babanrao Jamge")
print("PRN Number: RBTL25CB076")
print()

# =====================================================
# PR-8: TITANIC DATASET ANALYSIS
# =====================================================

print("=" * 70)
print("           TITANIC DATASET COMPREHENSIVE ANALYSIS")
print("=" * 70)

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')
print("\nDataset loaded successfully!")
print(f"Shape: {titanic.shape}")

print("\n--- First 5 Rows ---")
print(titanic.head())

print("\n--- Dataset Info ---")
print(titanic.info())

print("\n--- Statistical Summary ---")
print(titanic.describe())

# =====================================================
# 1. IDENTIFY FEATURES AND CLASSIFY BY DATA TYPE
# =====================================================

print("\n" + "=" * 70)
print("1. FEATURE IDENTIFICATION AND CLASSIFICATION")
print("=" * 70)

# Classify features by data type
numerical_features = titanic.select_dtypes(include=[np.number]).columns.tolist()
categorical_features = titanic.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()

print("\n--- Numerical Features ---")
for col in numerical_features:
    print(f"  • {col}: {titanic[col].dtype}")

print("\n--- Categorical Features ---")
for col in categorical_features:
    print(f"  • {col}: {titanic[col].dtype}")

# Chart type recommendations for each feature
print("\n--- Feature to Chart Type Mapping ---")
print(f"{'Feature':<20} {'Data Type':<15} {'Recommended Charts'}")
print("-" * 70)

for col in numerical_features:
    print(f"{col:<20} {'Numerical':<15} Histogram, Box Plot, Violin Plot, Scatter Plot")

for col in categorical_features:
    print(f"{col:<20} {'Categorical':<15} Bar Chart, Pie Chart, Count Plot")

# =====================================================
# 2. HISTOGRAMS AND BOX PLOTS FOR NUMERICAL FEATURES
# =====================================================

print("\n" + "=" * 70)
print("2. HISTOGRAMS AND BOX PLOTS (Numerical Features)")
print("=" * 70)

# Create histograms for all numerical features
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Histograms of Numerical Features - Titanic Dataset', fontsize=14)

for idx, col in enumerate(numerical_features[:6]):
    ax = axes[idx // 3, idx % 3]
    titanic[col].hist(ax=ax, bins=20, edgecolor='black', alpha=0.7)
    ax.set_title(f'{col}')
    ax.set_xlabel(col)
    ax.set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('titanic_histograms.png', dpi=100)
plt.show()

# Create box plots for all numerical features
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Box Plots of Numerical Features - Titanic Dataset', fontsize=14)

for idx, col in enumerate(numerical_features[:6]):
    ax = axes[idx // 3, idx % 3]
    titanic.boxplot(column=col, ax=ax)
    ax.set_title(f'{col}')

plt.tight_layout()
plt.savefig('titanic_boxplots.png', dpi=100)
plt.show()

# Outlier detection
print("\n--- Outlier Detection (IQR Method) ---")
for col in numerical_features:
    Q1 = titanic[col].quantile(0.25)
    Q3 = titanic[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = titanic[(titanic[col] < lower_bound) | (titanic[col] > upper_bound)][col]
    print(f"  {col}: {len(outliers)} outliers detected")

# =====================================================
# 3. SEABORN VISUALIZATIONS
# =====================================================

print("\n" + "=" * 70)
print("3. SEABORN VISUALIZATIONS")
print("=" * 70)

# Box plots using Seaborn
print("\nGenerating Box Plots...")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Seaborn Box Plots - Titanic Dataset', fontsize=14)

sns.boxplot(data=titanic, y='age', x='survived', ax=axes[0])
axes[0].set_title('Age by Survival')

sns.boxplot(data=titanic, y='fare', x='pclass', ax=axes[1])
axes[1].set_title('Fare by Class')

sns.boxplot(data=titanic, y='age', x='sex', ax=axes[2])
axes[2].set_title('Age by Sex')

plt.tight_layout()
plt.savefig('titanic_seaborn_boxplots.png', dpi=100)
plt.show()

# Violin plots
print("Generating Violin Plots...")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Violin Plots - Titanic Dataset', fontsize=14)

sns.violinplot(data=titanic, y='age', x='survived', ax=axes[0])
axes[0].set_title('Age Distribution by Survival')

sns.violinplot(data=titanic, y='fare', x='pclass', ax=axes[1])
axes[1].set_title('Fare Distribution by Class')

sns.violinplot(data=titanic, y='age', x='sex', ax=axes[2])
axes[2].set_title('Age Distribution by Sex')

plt.tight_layout()
plt.savefig('titanic_violin_plots.png', dpi=100)
plt.show()

# Pair plot
print("Generating Pair Plot...")
pair_cols = ['survived', 'pclass', 'age', 'fare']
sns.pairplot(titanic[pair_cols].dropna(), hue='survived', diag_kind='kde')
plt.suptitle('Pair Plot - Titanic Dataset', y=1.02)
plt.savefig('titanic_pairplot.png', dpi=100)
plt.show()

# Heatmap - Correlation Matrix
print("Generating Correlation Heatmap...")
plt.figure(figsize=(10, 8))
correlation_matrix = titanic[numerical_features].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=0.5, fmt='.2f')
plt.title('Correlation Heatmap - Titanic Dataset')
plt.savefig('titanic_heatmap.png', dpi=100)
plt.show()

# Correlation Analysis
print("\n--- Correlation Analysis ---")
print(correlation_matrix)

print("\n--- Key Correlations ---")
for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        col1 = correlation_matrix.columns[i]
        col2 = correlation_matrix.columns[j]
        corr_val = correlation_matrix.iloc[i, j]
        if abs(corr_val) > 0.3:
            strength = "Strong" if abs(corr_val) > 0.5 else "Moderate"
            direction = "Positive" if corr_val > 0 else "Negative"
            print(f"  {col1} vs {col2}: {corr_val:.3f} ({strength} {direction})")

# Missing Values Visualization
print("\nGenerating Missing Values Heatmap...")
plt.figure(figsize=(12, 6))
sns.heatmap(titanic.isnull(), cbar=True, yticklabels=False, cmap='viridis')
plt.title('Missing Values Heatmap - Titanic Dataset')
plt.savefig('titanic_missing_values.png', dpi=100)
plt.show()

print("\n--- Missing Values Summary ---")
missing = titanic.isnull().sum()
missing_pct = (missing / len(titanic)) * 100
for col in titanic.columns:
    if missing[col] > 0:
        print(f"  {col}: {missing[col]} ({missing_pct[col]:.2f}%)")

# =====================================================
# 4. COMPARE DISTRIBUTIONS AND IDENTIFY ANOMALIES
# =====================================================

print("\n" + "=" * 70)
print("4. DISTRIBUTION COMPARISON AND ANOMALY DETECTION")
print("=" * 70)

# Compare distributions
print("\nGenerating Distribution Comparisons...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Distribution Comparisons - Titanic Dataset', fontsize=14)

# Age distribution by survival
sns.histplot(data=titanic, x='age', hue='survived', kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Age Distribution by Survival')

# Fare distribution by class
sns.histplot(data=titanic, x='fare', hue='pclass', kde=True, ax=axes[0, 1])
axes[0, 1].set_title('Fare Distribution by Class')

# Age distribution by class
sns.histplot(data=titanic, x='age', hue='pclass', kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Age Distribution by Class')

# Survival count by sex
sns.countplot(data=titanic, x='sex', hue='survived', ax=axes[1, 1])
axes[1, 1].set_title('Survival Count by Sex')

plt.tight_layout()
plt.savefig('titanic_distribution_comparison.png', dpi=100)
plt.show()

# Identify anomalies
print("\n--- Anomaly Detection ---")
print("Anomalies in Fare:")
fare_anomalies = titanic[titanic['fare'] > titanic['fare'].quantile(0.99)]
print(f"  {len(fare_anomalies)} passengers paid extremely high fares (>99th percentile)")

print("\nAnomalies in Age:")
age_anomalies = titanic[titanic['age'] > 70]
print(f"  {len(age_anomalies)} passengers were above 70 years old")

# =====================================================
# GOOD AND BAD VISUALIZATION CRITIQUE
# =====================================================

print("\n" + "=" * 70)
print("VISUALIZATION CRITIQUE")
print("=" * 70)

print("\n--- THREE GOOD VISUALIZATIONS ---")
print("""
1. CORRELATION HEATMAP
   - Good because: Shows relationships between all numerical variables at once
   - Color coding makes it easy to identify strong/weak correlations
   - Annotations provide exact values for precise analysis

2. BOX PLOTS BY CATEGORY
   - Good because: Clearly shows distribution, median, quartiles, and outliers
   - Easy to compare different groups (e.g., survival vs non-survival)
   - Highlights data spread and identifies unusual values

3. PAIR PLOT WITH HUE
   - Good because: Shows relationships between multiple variables simultaneously
   - Diagonal plots show individual distributions
   - Color coding by category (survived) adds another dimension
""")

print("--- THREE BAD VISUALIZATION PRACTICES ---")
print("""
1. PIE CHART FOR MANY CATEGORIES
   - Bad because: Difficult to compare slice sizes when there are many categories
   - Human perception of angles is poor
   - Better alternative: Bar chart or treemap

2. 3D CHARTS FOR 2D DATA
   - Bad because: Adds unnecessary complexity and distorts perception
   - Occlusion can hide data points
   - Better alternative: 2D scatter plot or heatmap

3. TRUNCATED Y-AXIS
   - Bad because: Exaggerates differences and misleads the viewer
   - Can make small changes appear dramatic
   - Better alternative: Start Y-axis from zero or clearly indicate truncation
""")

# =====================================================
# 5. CHART TYPE RECOMMENDATION TABLE
# =====================================================

print("\n" + "=" * 70)
print("5. CHART TYPE RECOMMENDATION TABLE")
print("=" * 70)

recommendation_table = """
+----------------------+----------------------+----------------------------------+
| Data Type            | Purpose              | Recommended Chart Types          |
+----------------------+----------------------+----------------------------------+
| Numerical (Single)   | Distribution         | Histogram, Box Plot, Violin Plot |
| Numerical (Single)   | Outliers             | Box Plot, Strip Plot             |
| Numerical (Two)      | Relationship         | Scatter Plot, Line Plot          |
| Numerical (Multiple) | Correlation          | Heatmap, Pair Plot               |
| Categorical (Single) | Frequency            | Bar Chart, Pie Chart             |
| Categorical (Two)    | Comparison           | Grouped Bar, Stacked Bar         |
| Cat + Numerical      | Distribution Compare | Box Plot, Violin Plot, Swarm     |
| Time Series          | Trend                | Line Chart, Area Chart           |
| Time Series          | Seasonality          | Seasonal Decomposition Plot      |
| Proportions          | Parts of Whole       | Pie Chart, Donut, Treemap        |
| Hierarchical         | Nested Categories    | Treemap, Sunburst                |
| Geographical         | Location-based       | Choropleth Map, Bubble Map       |
+----------------------+----------------------+----------------------------------+
"""
print(recommendation_table)

# Save recommendation as DataFrame
chart_recommendations = pd.DataFrame({
    'Data Type': ['Numerical (Single)', 'Numerical (Single)', 'Numerical (Two)', 
                  'Numerical (Multiple)', 'Categorical (Single)', 'Categorical (Two)',
                  'Categorical + Numerical', 'Time Series', 'Proportions'],
    'Purpose': ['Distribution', 'Outliers', 'Relationship', 'Correlation', 
                'Frequency', 'Comparison', 'Distribution Comparison', 'Trend', 'Parts of Whole'],
    'Recommended Charts': ['Histogram, Box Plot, Violin Plot', 'Box Plot, Strip Plot',
                           'Scatter Plot, Line Plot', 'Heatmap, Pair Plot',
                           'Bar Chart, Pie Chart', 'Grouped Bar, Stacked Bar',
                           'Box Plot, Violin Plot', 'Line Chart, Area Chart',
                           'Pie Chart, Treemap']
})

print("\n--- Recommendation Table as DataFrame ---")
print(chart_recommendations.to_string(index=False))

print("\n" + "=" * 70)
print("           TITANIC DATASET ANALYSIS COMPLETE!")
print("=" * 70)
