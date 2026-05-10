# Step 1 - Import Libraries

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

# Step 2 - Load Dataset

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

col_names = ['Sepal_Length', 'Sepal_Width',
             'Petal_Length', 'Petal_Width',
             'Species']

df = pd.read_csv(url, names=col_names)

# Step 3 - Display Dataset

print("First 5 Rows")
print(df.head())

# Step 4 - Check Shape

print("\nShape of Dataset")
print(df.shape)

# Step 5 - Check Data Types

print("\nData Types")
print(df.dtypes)

# Step 6 - Statistical Information

print("\nStatistical Summary")
print(df.describe())

# Step 7 - Check Missing Values

print("\nMissing Values")
print(df.isnull().sum())

# Step 8 - Label Encoding

label_encoder = preprocessing.LabelEncoder()

df['Species'] = label_encoder.fit_transform(df['Species'])

print("\nAfter Label Encoding")
print(df.head())

# Step 9 - Normalization

scaler = MinMaxScaler()

x = df.iloc[:, :4]

x_scaled = scaler.fit_transform(x)

df_normalized = pd.DataFrame(x_scaled,
                             columns=['Sepal_Length',
                                      'Sepal_Width',
                                      'Petal_Length',
                                      'Petal_Width'])

print("\nNormalized Data")
print(df_normalized.head())