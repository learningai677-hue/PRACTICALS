# Step 1 - Import Required Libraries

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Step 2 - Load Boston Housing Dataset

df = pd.read_csv("HousingData.csv")


# Step 3 - Display Dataset

print("First 5 Rows")
print(df.head())


# Step 4 - Display Shape of Dataset

print("\nShape of Dataset")
print(df.shape)


# Step 5 - Check Missing Values

print("\nMissing Values")
print(df.isnull().sum())


# Step 6 - Fill Missing Values

df.fillna(df.mean(), inplace=True)

print("\nDataset after filling missing values")
print(df.head())


# Step 7 - Define Independent and Dependent Variables

# Independent Variables
X = df.drop('MEDV', axis=1)

# Dependent Variable
y = df['MEDV']


# Step 8 - Split Dataset into Training and Testing Data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Step 9 - Create Linear Regression Model

model = LinearRegression()


# Step 10 - Train Model

model.fit(X_train, y_train)


# Step 11 - Predict Values

y_pred = model.predict(X_test)


# Step 12 - Display Predicted Values

print("\nPredicted Values")
print(y_pred)


# Step 13 - Display Actual Values

print("\nActual Values")
print(y_test.values)


# Step 14 - Display Model Coefficients

print("\nModel Coefficients")
print(model.coef_)


# Step 15 - Display Intercept

print("\nModel Intercept")
print(model.intercept_)


# Step 16 - Display Accuracy Score

score = model.score(X_test, y_test)

print("\nModel Accuracy")
print(score)