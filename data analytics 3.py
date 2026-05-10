# Step 1 - Import Required Libraries

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


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


# Step 5 - Check Missing Values

print("\nMissing Values")
print(df.isnull().sum())


# Step 6 - Define Independent and Dependent Variables

X = df.iloc[:, :-1]

y = df.iloc[:, -1]


# Step 7 - Split Dataset into Training and Testing Data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# Step 8 - Create Naive Bayes Model

model = GaussianNB()


# Step 9 - Train Model

model.fit(X_train, y_train)


# Step 10 - Predict Values

y_pred = model.predict(X_test)


# Step 11 - Display Predicted Values

print("\nPredicted Values")
print(y_pred)


# Step 12 - Create Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print(cm)


# Step 13 - Calculate Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy")
print(accuracy)


# Step 14 - Calculate Precision

precision = precision_score(
    y_test,
    y_pred,
    average='macro'
)

print("\nPrecision")
print(precision)


# Step 15 - Calculate Recall

recall = recall_score(
    y_test,
    y_pred,
    average='macro'
)

print("\nRecall")
print(recall)


# Step 16 - Calculate Error Rate

error_rate = 1 - accuracy

print("\nError Rate")
print(error_rate)