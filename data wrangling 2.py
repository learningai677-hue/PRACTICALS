# Step 1 - Import Libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2 - Create Dataset

data = {
    'Math_Score': [85, 90, np.nan, 40, 95, 100, 35, 88, 76, 300],
    'Reading_Score': [80, 85, 78, 45, 92, 98, 30, np.nan, 74, 110],
    'Placement_Score': [78, 85, 80, 50, 95, 99, 45, 82, 70, 200]
}

df = pd.DataFrame(data)

# Step 3 - Display Dataset

print("Dataset")
print(df)

# Step 4 - Check Missing Values

print("\nMissing Values")
print(df.isnull().sum())

# Step 5 - Fill Missing Values

df.fillna(df.mean(), inplace=True)

print("\nDataset after filling missing values")
print(df)

# Step 6 - Detect Outliers using Boxplot

sns.boxplot(data=df)

plt.title("Boxplot for Outlier Detection")
plt.show()

# Step 7 - Remove Outliers using IQR Method

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)

IQR = Q3 - Q1

df_no_outlier = df[~((df < (Q1 - 1.5 * IQR)) |
                     (df > (Q3 + 1.5 * IQR))).any(axis=1)]

print("\nDataset after removing outliers")
print(df_no_outlier)

# Step 8 - Apply Log Transformation

df_transformed = np.log(df_no_outlier)

print("\nLog Transformed Data")
print(df_transformed)