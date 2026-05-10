        # Step 1 - Import Required Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Step 2 - Load Iris Dataset

df = sns.load_dataset('iris')


# Step 3 - Display Dataset

print("First 5 Rows")
print(df.head())


# Step 4 - Display Shape of Dataset

print("\nShape of Dataset")
print(df.shape)


# Step 5 - Check Missing Values

print("\nMissing Values")
print(df.isnull().sum())


# Step 6 - Display Data Types

print("\nData Types")
print(df.dtypes)


# Step 7 - Display Statistical Summary

print("\nStatistical Summary")
print(df.describe())


# Step 8 - Display Features

print("\nFeatures in Dataset")
print(df.columns)


# Step 9 - Plot Histograms for Each Feature

df.hist(figsize=(10,8))

plt.suptitle("Histogram of Iris Dataset Features")

plt.show()


# Step 10 - Plot Boxplots for Each Feature

plt.figure(figsize=(10,8))

sns.boxplot(data=df)

plt.title("Boxplot of Iris Dataset Features")

plt.show()