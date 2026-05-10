# Step 1 - Import Required Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Step 2 - Load Titanic Dataset

df = sns.load_dataset('titanic')


# Step 3 - Display Dataset

print("First 5 Rows")
print(df.head())


# Step 4 - Display Shape of Dataset

print("\nShape of Dataset")
print(df.shape)


# Step 5 - Check Missing Values

print("\nMissing Values")
print(df.isnull().sum())


# Step 6 - Display Statistical Summary

print("\nStatistical Summary")
print(df.describe())


# Step 7 - Plot Boxplot

plt.figure(figsize=(8,5))

sns.boxplot(
    x='sex',
    y='age',
    hue='survived',
    data=df
)

plt.title("Age Distribution with Respect to Gender and Survival")

plt.xlabel("Gender")

plt.ylabel("Age")

plt.show()