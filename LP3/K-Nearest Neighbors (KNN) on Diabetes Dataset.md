Mate, this is a Machine Learning practical using **K-Nearest Neighbors (KNN)** for diabetes classification. We'll use `scikit-learn` and keep the program clean, straightforward, and easy to memorize.

# **Experiment: K-Nearest Neighbors (KNN) on Diabetes Dataset**

**Aim:** To implement the K-Nearest Neighbors algorithm on the `diabetes.csv` dataset and calculate the confusion matrix, accuracy, error rate, precision, and recall.

## **1. Python Program**

```
# KNN Algorithm on Diabetes Datasetimport pandas as pdfrom sklearn.model_selection import train_test_splitfrom sklearn.preprocessing import StandardScalerfrom sklearn.neighbors import KNeighborsClassifierfrom sklearn.metrics import confusion_matrix, accuracy_scorefrom sklearn.metrics import precision_score, recall_score# Load datasetdata = pd.read_csv("diabetes.csv")# Split features and targetX = data.drop("Outcome", axis=1)y = data["Outcome"]# Split dataset into training and testing dataX_train, X_test, y_train, y_test = train_test_split(    X, y, test_size=0.2, random_state=42)# Feature scalingscaler = StandardScaler()X_train = scaler.fit_transform(X_train)X_test = scaler.transform(X_test)# Create KNN modelknn = KNeighborsClassifier(n_neighbors=5)# Train the modelknn.fit(X_train, y_train)# Predict the outputy_pred = knn.predict(X_test)# Calculate performance metricscm = confusion_matrix(y_test, y_pred)accuracy = accuracy_score(y_test, y_pred)error_rate = 1 - accuracyprecision = precision_score(y_test, y_pred)recall = recall_score(y_test, y_pred)# Display resultsprint("Confusion Matrix:\n", cm)print("Accuracy:", accuracy)print("Error Rate:", error_rate)print("Precision:", precision)print("Recall:", recall)
```

## **2. Sample Output**

The following is an illustrative output format. Actual values depend on the dataset and train-test split.

```
Confusion Matrix:
[[85 14]
 [18 37]]

Accuracy: 0.7922
Error Rate: 0.2078
Precision: 0.7255
Recall: 0.6727
```

## **3. Theory**

### **What is K-Nearest Neighbors (KNN)?**

K-Nearest Neighbors is a supervised machine learning algorithm used for classification and regression.

It classifies a new data point based on the majority class of its K nearest neighboring data points.

In this practical, KNN is used to predict whether a person has diabetes or not.

Class AClass BPredictionClass A

k = 5: Class A wins 3–2; the point is Class A.

\\(k\\)

Give feedback

### **Working of KNN Algorithm**

1. Load the diabetes dataset.
2. Divide the dataset into training and testing data.
3. Select the value of K (here, K = 5).
4. Calculate the distance between the new data point and training data points.
5. Find the K nearest neighbors.
6. Assign the class based on majority voting.
7. Evaluate the model using performance metrics.

### **4. Important Formulas**

**1. Euclidean Distance**

Used to calculate the distance between two data points.

\\[ d=\sqrt{\sum\_{i=1}^{n}(x_i-y_i)^2} \\]

**2. Confusion Matrix**

A confusion matrix evaluates the performance of a classification model.

|                 | Predicted Positive | Predicted Negative |
| --------------- | ------------------ | ------------------ |
| Actual Positive | TP                 | FN                 |
| Actual Negative | FP                 | TN                 |

- TP = True Positive
- TN = True Negative
- FP = False Positive
- FN = False Negative

**3. Accuracy**

Measures the percentage of correctly classified predictions.

\\[ Accuracy=\frac{TP+TN}{TP+TN+FP+FN} \\]

**4. Error Rate**

Measures the percentage of incorrect predictions.

\\[ Error\ Rate=1-Accuracy \\]

**5. Precision**

Measures how many predicted positive cases are actually positive.

\\[ Precision=\frac{TP}{TP+FP} \\]

**6. Recall**

Measures how many actual positive cases are correctly identified.

\\[ Recall=\frac{TP}{TP+FN} \\]

## **5. Explanation of Important Python Functions**

| Function                 | Purpose                                     |
| ------------------------ | ------------------------------------------- |
| `read_csv()`             | Loads the dataset                           |
| `train_test_split()`     | Divides data into training and testing sets |
| `StandardScaler()`       | Scales the features                         |
| `KNeighborsClassifier()` | Creates the KNN model                       |
| `fit()`                  | Trains the model                            |
| `predict()`              | Predicts the output                         |
| `confusion_matrix()`     | Generates confusion matrix                  |
| `accuracy_score()`       | Calculates accuracy                         |
| `precision_score()`      | Calculates precision                        |
| `recall_score()`         | Calculates recall                           |

## **6. Time and Space Complexity**

- **Training Time:** Approximately O(1), excluding data preparation, because standard KNN mainly stores the training data.
- **Prediction Time:** O(n × d) per query, where n is the number of training samples and d is the number of features.
- **Space Complexity:** O(n × d), for storing the training dataset.

## **7. Result**

Thus, the K-Nearest Neighbors algorithm was successfully implemented on the diabetes dataset, and its performance was evaluated using the confusion matrix, accuracy, error rate, precision, and recall.

## **Important Viva Questions**

**1. What is KNN?**

KNN is a supervised machine learning algorithm that classifies data based on the majority class of its nearest neighbors.

**2. What does K represent in KNN?**

K represents the number of nearest neighbors considered for classification.

**3. Why do we use K = 5?**

K = 5 is a commonly used starting choice. The optimal K can be determined through experimentation.

**4. What is the purpose of StandardScaler?**

It standardizes the features so that variables with larger numerical values do not dominate distance calculations.

**5. What is the difference between supervised and unsupervised learning?**

| Supervised Learning                    | Unsupervised Learning    |
| -------------------------------------- | ------------------------ |
| Uses labelled data                     | Uses unlabelled data     |
| Has known output                       | Has no predefined output |
| Used for classification and regression | Used for clustering      |
| Example: KNN                           | Example: K-Means         |

**6. Why is KNN called a lazy learning algorithm?**

Because it does not build an explicit model during training. It stores the training data and performs calculations when a prediction is required.

**7. What happens if K is too small?**

The model may become sensitive to noise and overfit.

**8. What happens if K is too large?**

The model may become overly generalized and underfit.

### **Five things to memorize before the practical**

1. `train_test_split()` – split the dataset.
2. `StandardScaler()` – scale the features.
3. `KNeighborsClassifier(n_neighbors=5)` – create the model.
4. `knn.fit()` and `knn.predict()` – train and predict.
5. `confusion_matrix()`, `accuracy_score()`, `precision_score()`, `recall_score()` – evaluate.

**One important exam detail:** The diabetes dataset commonly uses `Outcome` as its target column, where 0 means non-diabetic and 1 means diabetic. Also, scaling is particularly important for KNN because it relies on distance calculations.
