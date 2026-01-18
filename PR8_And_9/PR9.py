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
# PR-9: IRIS DATASET COMPREHENSIVE ANALYSIS
# =====================================================

print("=" * 70)
print("           IRIS DATASET COMPREHENSIVE ANALYSIS")
print("=" * 70)

# Load the Iris dataset
iris = sns.load_dataset('iris')
print("\nDataset loaded successfully!")
print(f"Shape: {iris.shape}")

print("\n--- First 5 Rows ---")
print(iris.head())

print("\n--- Dataset Info ---")
print(iris.info())

print("\n--- Statistical Summary ---")
print(iris.describe())

# =====================================================
# 1. IDENTIFY FEATURES AND CLASSIFY BY DATA TYPE
# =====================================================

print("\n" + "=" * 70)
print("1. FEATURE IDENTIFICATION AND CLASSIFICATION")
print("=" * 70)

# Classify features by data type
numerical_features = iris.select_dtypes(include=[np.number]).columns.tolist()
categorical_features = iris.select_dtypes(include=['object', 'category']).columns.tolist()

print("\n--- Numerical Features ---")
for col in numerical_features:
    print(f"  • {col}: {iris[col].dtype} (Continuous)")

print("\n--- Categorical Features ---")
for col in categorical_features:
    unique_vals = iris[col].nunique()
    print(f"  • {col}: {iris[col].dtype} ({unique_vals} unique values)")

# Chart type recommendations for each feature
print("\n--- Feature to Chart Type Mapping ---")
print(f"{'Feature':<20} {'Data Type':<15} {'Recommended Charts'}")
print("-" * 70)

for col in numerical_features:
    print(f"{col:<20} {'Numerical':<15} Histogram, Box Plot, Violin Plot, Scatter Plot")

for col in categorical_features:
    print(f"{col:<20} {'Categorical':<15} Bar Chart, Pie Chart, Count Plot")

print(f"{'species + numerical':<20} {'Mixed':<15} Grouped Box Plot, Violin Plot, Swarm Plot")

# =====================================================
# 2. HISTOGRAMS AND BOX PLOTS FOR NUMERICAL FEATURES
# =====================================================

print("\n" + "=" * 70)
print("2. HISTOGRAMS AND BOX PLOTS (Numerical Features)")
print("=" * 70)

# Create histograms for all numerical features
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Histograms of Numerical Features - Iris Dataset', fontsize=14)

for idx, col in enumerate(numerical_features):
    ax = axes[idx // 2, idx % 2]
    iris[col].hist(ax=ax, bins=20, edgecolor='black', alpha=0.7, color='steelblue')
    ax.set_title(f'{col}')
    ax.set_xlabel(col)
    ax.set_ylabel('Frequency')
    ax.axvline(iris[col].mean(), color='red', linestyle='--', label=f'Mean: {iris[col].mean():.2f}')
    ax.axvline(iris[col].median(), color='green', linestyle='--', label=f'Median: {iris[col].median():.2f}')
    ax.legend()

plt.tight_layout()
plt.savefig('iris_histograms.png', dpi=100)
plt.show()

# Create box plots for all numerical features
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Box Plots of Numerical Features - Iris Dataset', fontsize=14)

for idx, col in enumerate(numerical_features):
    ax = axes[idx // 2, idx % 2]
    iris.boxplot(column=col, ax=ax)
    ax.set_title(f'{col}')

plt.tight_layout()
plt.savefig('iris_boxplots.png', dpi=100)
plt.show()

# Outlier detection
print("\n--- Outlier Detection (IQR Method) ---")
for col in numerical_features:
    Q1 = iris[col].quantile(0.25)
    Q3 = iris[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = iris[(iris[col] < lower_bound) | (iris[col] > upper_bound)][col]
    print(f"  {col}:")
    print(f"    Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
    print(f"    Lower Bound: {lower_bound:.2f}, Upper Bound: {upper_bound:.2f}")
    print(f"    Outliers: {len(outliers)} detected")

# =====================================================
# 3. SEABORN VISUALIZATIONS
# =====================================================

print("\n" + "=" * 70)
print("3. SEABORN VISUALIZATIONS")
print("=" * 70)

# Box plots using Seaborn (by species)
print("\nGenerating Box Plots by Species...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Box Plots by Species - Iris Dataset', fontsize=14)

for idx, col in enumerate(numerical_features):
    ax = axes[idx // 2, idx % 2]
    sns.boxplot(data=iris, x='species', y=col, ax=ax, palette='Set2')
    ax.set_title(f'{col} by Species')

plt.tight_layout()
plt.savefig('iris_seaborn_boxplots.png', dpi=100)
plt.show()

# Violin plots
print("Generating Violin Plots...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Violin Plots by Species - Iris Dataset', fontsize=14)

for idx, col in enumerate(numerical_features):
    ax = axes[idx // 2, idx % 2]
    sns.violinplot(data=iris, x='species', y=col, ax=ax, palette='Set3')
    ax.set_title(f'{col} Distribution by Species')

plt.tight_layout()
plt.savefig('iris_violin_plots.png', dpi=100)
plt.show()

# Pair plot
print("Generating Pair Plot...")
sns.pairplot(iris, hue='species', diag_kind='kde', palette='husl')
plt.suptitle('Pair Plot - Iris Dataset', y=1.02)
plt.savefig('iris_pairplot.png', dpi=100)
plt.show()

# Heatmap - Correlation Matrix
print("Generating Correlation Heatmap...")
plt.figure(figsize=(10, 8))
correlation_matrix = iris[numerical_features].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=0.5, fmt='.3f',
            annot_kws={'size': 12})
plt.title('Correlation Heatmap - Iris Dataset', fontsize=14)
plt.savefig('iris_heatmap.png', dpi=100)
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
        strength = "Strong" if abs(corr_val) > 0.7 else "Moderate" if abs(corr_val) > 0.4 else "Weak"
        direction = "Positive" if corr_val > 0 else "Negative"
        print(f"  {col1} vs {col2}: {corr_val:.3f} ({strength} {direction})")

# Swarm Plot
print("\nGenerating Swarm Plots...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Swarm Plots by Species - Iris Dataset', fontsize=14)

for idx, col in enumerate(numerical_features):
    ax = axes[idx // 2, idx % 2]
    sns.swarmplot(data=iris, x='species', y=col, ax=ax, palette='Set1')
    ax.set_title(f'{col} by Species')

plt.tight_layout()
plt.savefig('iris_swarm_plots.png', dpi=100)
plt.show()

# Missing Values Visualization
print("\nGenerating Missing Values Heatmap...")
plt.figure(figsize=(10, 6))
sns.heatmap(iris.isnull(), cbar=True, yticklabels=False, cmap='viridis')
plt.title('Missing Values Heatmap - Iris Dataset')
plt.savefig('iris_missing_values.png', dpi=100)
plt.show()

print("\n--- Missing Values Summary ---")
missing = iris.isnull().sum()
if missing.sum() == 0:
    print("  No missing values in the dataset!")
else:
    for col in iris.columns:
        if missing[col] > 0:
            print(f"  {col}: {missing[col]} ({(missing[col]/len(iris))*100:.2f}%)")

# =====================================================
# 4. COMPARE DISTRIBUTIONS AND IDENTIFY ANOMALIES
# =====================================================

print("\n" + "=" * 70)
print("4. DISTRIBUTION COMPARISON AND ANOMALY DETECTION")
print("=" * 70)

# Compare distributions
print("\nGenerating Distribution Comparisons...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Distribution Comparisons by Species - Iris Dataset', fontsize=14)

for idx, col in enumerate(numerical_features):
    ax = axes[idx // 2, idx % 2]
    for species in iris['species'].unique():
        species_data = iris[iris['species'] == species][col]
        sns.kdeplot(data=species_data, ax=ax, label=species, fill=True, alpha=0.3)
    ax.set_title(f'{col} Distribution by Species')
    ax.legend()

plt.tight_layout()
plt.savefig('iris_distribution_comparison.png', dpi=100)
plt.show()

# Species-wise statistics
print("\n--- Species-wise Statistics ---")
for species in iris['species'].unique():
    species_data = iris[iris['species'] == species]
    print(f"\n{species.upper()}:")
    for col in numerical_features:
        print(f"  {col}: Mean={species_data[col].mean():.2f}, Std={species_data[col].std():.2f}")

# Identify anomalies
print("\n--- Anomaly Detection ---")
for col in numerical_features:
    Q1 = iris[col].quantile(0.25)
    Q3 = iris[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = iris[(iris[col] < lower_bound) | (iris[col] > upper_bound)]
    if len(outliers) > 0:
        print(f"\n  Outliers in {col}:")
        for idx, row in outliers.iterrows():
            print(f"    Index {idx}: {row[col]:.2f} (Species: {row['species']})")

# =====================================================
# GOOD AND BAD VISUALIZATION CRITIQUE
# =====================================================

print("\n" + "=" * 70)
print("VISUALIZATION CRITIQUE")
print("=" * 70)

print("\n--- THREE GOOD VISUALIZATIONS ---")
print("""
1. PAIR PLOT WITH SPECIES HUE
   - Good because: Shows all pairwise relationships at once
   - Diagonal KDE plots show individual distributions per species
   - Clear separation between species visible in some feature pairs
   - Great for identifying which features best distinguish classes

2. VIOLIN PLOT BY SPECIES
   - Good because: Combines box plot with kernel density estimation
   - Shows full distribution shape, not just summary statistics
   - Easy to compare distributions across species
   - Reveals multimodal distributions if present

3. CORRELATION HEATMAP
   - Good because: Compact visualization of all correlations
   - Color intensity immediately shows correlation strength
   - Numeric annotations provide precise values
   - Square shape makes symmetry apparent
""")

print("--- THREE BAD VISUALIZATION PRACTICES ---")
print("""
1. USING TOO MANY COLORS
   - Bad because: Makes it hard to distinguish categories
   - Can cause cognitive overload
   - Accessibility issues for colorblind viewers
   - Better alternative: Use max 5-7 distinct colors

2. OVERLAPPING HISTOGRAMS WITHOUT TRANSPARENCY
   - Bad because: Hides data behind other bars
   - Difficult to see actual distribution of each category
   - Better alternative: Use KDE plots or set alpha transparency

3. MISLEADING AXIS SCALES
   - Bad because: Can exaggerate or minimize differences
   - Comparing charts with different scales is deceptive
   - Better alternative: Use consistent scales or clearly label differences
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

# Iris-specific recommendations
print("\n--- Iris Dataset Specific Recommendations ---")
iris_recommendations = pd.DataFrame({
    'Analysis Goal': [
        'Compare sepal/petal sizes',
        'Identify species clusters',
        'Detect outliers',
        'Show feature correlations',
        'Compare distributions',
        'Show species counts'
    ],
    'Best Chart Type': [
        'Scatter Plot (sepal_length vs sepal_width)',
        'Pair Plot with species hue',
        'Box Plot by species',
        'Correlation Heatmap',
        'Violin Plot or KDE Plot',
        'Bar Chart or Count Plot'
    ],
    'Why': [
        'Shows relationship and species separation',
        'Reveals clustering in feature space',
        'IQR-based outlier visualization',
        'Compact view of all relationships',
        'Shows full distribution shape',
        'Easy comparison of frequencies'
    ]
})
print(iris_recommendations.to_string(index=False))

# Final scatter plot showing species separation
print("\nGenerating Final Scatter Plot (Best Features for Classification)...")
plt.figure(figsize=(10, 8))
for species in iris['species'].unique():
    species_data = iris[iris['species'] == species]
    plt.scatter(species_data['petal_length'], species_data['petal_width'], 
                label=species, alpha=0.7, s=60)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Iris Species Classification - Petal Dimensions')
plt.legend(title='Species')
plt.grid(True, alpha=0.3)
plt.savefig('iris_classification_scatter.png', dpi=100)
plt.show()

print("\n" + "=" * 70)
print("           IRIS DATASET ANALYSIS COMPLETE!")
print("=" * 70)
