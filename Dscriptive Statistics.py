# Step 1 - Import Required Libraries

import pandas as pd
import numpy as np


# Step 2 - Load Iris Dataset

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

col_names = ['Sepal_Length',
             'Sepal_Width',
             'Petal_Length',
             'Petal_Width',
             'Species']

df = pd.read_csv(url, names=col_names)


# Step 3 - Display Dataset

print("First 5 Rows")
print(df.head())


# Step 4 - Display Shape of Dataset

print("\nShape of Dataset")
print(df.shape)


# Step 5 - Display Data Types

print("\nData Types")
print(df.dtypes)


# Step 6 - Display Statistical Summary

print("\nStatistical Summary")
print(df.describe())


# Step 7 - Display Unique Species

print("\nUnique Species")
print(df['Species'].unique())


# Step 8 - Count Species Values

print("\nSpecies Count")
print(df['Species'].value_counts())


# Step 9 - Create Separate DataFrames

iris_setosa = df[df['Species'] == 'Iris-setosa']

iris_versicolor = df[df['Species'] == 'Iris-versicolor']

iris_virginica = df[df['Species'] == 'Iris-virginica']


# Step 10 - Mean Values

print("\nMean of Iris Setosa")
print(iris_setosa.mean(numeric_only=True))

print("\nMean of Iris Versicolor")
print(iris_versicolor.mean(numeric_only=True))

print("\nMean of Iris Virginica")
print(iris_virginica.mean(numeric_only=True))


# Step 11 - Median Values

print("\nMedian of Iris Setosa")
print(iris_setosa.median(numeric_only=True))

print("\nMedian of Iris Versicolor")
print(iris_versicolor.median(numeric_only=True))

print("\nMedian of Iris Virginica")
print(iris_virginica.median(numeric_only=True))


# Step 12 - Minimum Values

print("\nMinimum Values of Iris Setosa")
print(iris_setosa.min(numeric_only=True))

print("\nMinimum Values of Iris Versicolor")
print(iris_versicolor.min(numeric_only=True))

print("\nMinimum Values of Iris Virginica")
print(iris_virginica.min(numeric_only=True))


# Step 13 - Maximum Values

print("\nMaximum Values of Iris Setosa")
print(iris_setosa.max(numeric_only=True))

print("\nMaximum Values of Iris Versicolor")
print(iris_versicolor.max(numeric_only=True))

print("\nMaximum Values of Iris Virginica")
print(iris_virginica.max(numeric_only=True))


# Step 14 - Standard Deviation

print("\nStandard Deviation of Iris Setosa")
print(iris_setosa.std(numeric_only=True))

print("\nStandard Deviation of Iris Versicolor")
print(iris_versicolor.std(numeric_only=True))

print("\nStandard Deviation of Iris Virginica")
print(iris_virginica.std(numeric_only=True))


# Step 15 - Percentile Calculation

print("\n25th Percentile")
print(df.quantile(0.25, numeric_only=True))

print("\n50th Percentile")
print(df.quantile(0.50, numeric_only=True))

print("\n75th Percentile")
print(df.quantile(0.75, numeric_only=True))