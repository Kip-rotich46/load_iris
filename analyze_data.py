import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add target column (species)
df['species'] = iris.target

# Display the first few rows of the dataset
print(df.head())

# Check the structure of the dataset (data types and missing values)
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Clean the dataset (if necessary, fill missing values)
df.fillna(df.mean(), inplace=True)

# Task 2: Basic Data Analysis

# Compute basic statistics for numerical columns
print("\nBasic Statistics:")
print(df.describe())

# Group by species and compute mean for each group
grouped = df.groupby('species').mean()
print("\nGrouped by Species (Mean of Numerical Columns):")
print(grouped)

# Task 3: Data Visualization

# Line Chart: Trend of Sepal Length
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['sepal length (cm)'])
plt.title('Trend of Sepal Length')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.show()

# Bar Chart: Average Sepal Length per Species
species_avg_sepal_length = df.groupby('species')['sepal length (cm)'].mean()
plt.figure(figsize=(10, 6))
species_avg_sepal_length.plot(kind='bar')
plt.title('Average Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')
plt.xticks(rotation=0)
plt.show()

# Histogram: Distribution of Sepal Length
plt.figure(figsize=(10, 6))
df['sepal length (cm)'].hist(bins=20)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(10, 6))
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'])
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()

# Task 4: Error Handling for File Loading
try:
    df = pd.read_csv('dataset.csv')
except FileNotFoundError:
    print("The file does not exist!")
except pd.errors.EmptyDataError:
    print("The file is empty!")
except Exception as e:
    print(f"An error occurred: {e}")
