Mate, this practical is about **Email Spam Detection using Binary Classification**. We'll implement both K-Nearest Neighbors (KNN) and Support Vector Machine (SVM), then compare their performance.

We'll use a simple dataset containing email text and spam labels. The program uses TF-IDF to convert email text into numerical features.

# **Experiment: Email Spam Detection Using KNN and SVM**

**Aim:** To classify emails into two categories (Spam and Not Spam) using K-Nearest Neighbors and Support Vector Machine algorithms and compare their performance.

## **1. Python Program**

```
# Email Spam Detection using KNN and SVMimport pandas as pdfrom sklearn.model_selection import train_test_splitfrom sklearn.feature_extraction.text import TfidfVectorizerfrom sklearn.neighbors import KNeighborsClassifierfrom sklearn.svm import SVCfrom sklearn.metrics import accuracy_score, confusion_matrixfrom sklearn.metrics import precision_score, recall_score# Load datasetdata = pd.read_csv("spam.csv", encoding='latin-1')# Select email text and labelsX = data['v2']y = data['v1']# Convert labels into binary valuesy = y.map({'ham': 0, 'spam': 1})# Convert email text into numerical featurestfidf = TfidfVectorizer(stop_words='english')X = tfidf.fit_transform(X)# Split datasetX_train, X_test, y_train, y_test = train_test_split(    X, y, test_size=0.2, random_state=42)# KNN Classificationknn = KNeighborsClassifier(n_neighbors=5)knn.fit(X_train, y_train)knn_pred = knn.predict(X_test)# SVM Classificationsvm = SVC(kernel='linear')svm.fit(X_train, y_train)svm_pred = svm.predict(X_test)# Function to evaluate modeldef evaluate_model(name, y_test, y_pred):    print("\n", name)    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))    print("Accuracy:", accuracy_score(y_test, y_pred))    print("Precision:", precision_score(y_test, y_pred))    print("Recall:", recall_score(y_test, y_pred))# Evaluate both modelsevaluate_model("KNN Performance", y_test, knn_pred)evaluate_model("SVM Performance", y_test, svm_pred)
```

## **2. Sample Output**

The following is an illustrative output. Actual values depend on the dataset and train-test split.

```
KNN Performance

Confusion Matrix:
[[965   0]
 [ 20 130]]

Accuracy: 0.982
Precision: 1.0
Recall: 0.867

SVM Performance

Confusion Matrix:
[[965   0]
 [  5 145]]

Accuracy: 0.996
Precision: 1.0
Recall: 0.967
```

## **3. Theory**

### **What is Binary Classification?**

Binary classification is a supervised machine learning technique used to classify data into two distinct categories.

In email spam detection, there are two states:

- **Normal State (0):** Not Spam (Ham).
- **Abnormal State (1):** Spam.

The objective is to identify whether an incoming email is legitimate or unwanted.

### **What is K-Nearest Neighbors (KNN)?**

KNN is a supervised machine learning algorithm that classifies a new data point based on the majority class of its K nearest neighbors.

**Working:**

1. Select the value of K.
2. Calculate the distance between data points.
3. Identify the K nearest neighbors.
4. Count the classes of the nearest neighbors.
5. Assign the majority class as the predicted output.

Class AClass BPredictionClass A

k = 5: Class A wins 3–2; the point is Class A.

\\(k\\)

Give feedback

### **What is Support Vector Machine (SVM)?**

SVM is a supervised machine learning algorithm used for classification and regression.

It finds an optimal decision boundary called a **hyperplane** that separates different classes.

**Working:**

1. Represent email data as numerical features.
2. Identify the decision boundary between spam and normal emails.
3. Find support vectors closest to the boundary.
4. Construct the optimal hyperplane.
5. Classify new emails based on which side of the hyperplane they fall on.

[Support Vector Machine In Machine Learning Algorithms | by Dhivya | Medium](https://images.openai.com/static-rsc-4/yP0w4OBjsIOGJ4jRm4ErwAYjU2evAyvu77PbdJiJr69_AWUcVQL6TfwotFc8TLPy9cYaVbb00-DQSHierr1NjkCEtX92mNWZA8jCLgJGPnkzZmYa5kFIWFW9p-tS34csa0qkoFL1fsMaxhI_077wdr0iVlx4xeKC5mM6oh5KW2s?purpose=inline)

[medium.com](https://medium.com/%40dhivyasamin/support-vector-machine-in-machine-learning-algorithms-3fd8f399e0c2?utm_source=chatgpt.com)

## **4. TF-IDF Vectorization**

Computers cannot directly understand email text. Therefore, we convert text into numerical features using TF-IDF.

TF-IDF stands for Term Frequency–Inverse Document Frequency.

It assigns importance to words based on their frequency in an email and how common they are across all emails.

This helps the machine learning algorithms process email content.

## **5. Performance Evaluation**

We evaluate both algorithms using the following metrics:

**1. Accuracy**

Measures the percentage of correctly classified emails.

\\[ Accuracy=\frac{TP+TN}{TP+TN+FP+FN} \\]

**2. Precision**

Measures how many emails predicted as spam are actually spam.

\\[ Precision=\frac{TP}{TP+FP} \\]

**3. Recall**

Measures how many actual spam emails are correctly identified.

\\[ Recall=\frac{TP}{TP+FN} \\]

**4. Confusion Matrix**

|                 | Predicted Not Spam | Predicted Spam |
| --------------- | ------------------ | -------------- |
| Actual Not Spam | TN                 | FP             |
| Actual Spam     | FN                 | TP             |

## **6. Comparison Between KNN and SVM**

| KNN                                     | SVM                                             |
| --------------------------------------- | ----------------------------------------------- |
| Uses nearest neighbors                  | Uses optimal hyperplane                         |
| Distance-based algorithm                | Margin-based algorithm                          |
| Lazy learning algorithm                 | Model-based learning                            |
| Prediction can be slower                | Prediction is generally faster after training   |
| Sensitive to feature scaling            | Also benefits from feature scaling              |
| Can struggle with high-dimensional data | Often effective with high-dimensional text data |

### **Performance Analysis**

- KNN classifies emails based on their nearest neighboring emails.
- SVM classifies emails by finding an optimal decision boundary.
- Accuracy, precision, recall and confusion matrix are used to compare both models.
- SVM often performs well on high-dimensional text data, although actual performance depends on the dataset and parameter settings.

## **7. Result**

Thus, email spam detection was successfully implemented using K-Nearest Neighbors and Support Vector Machine algorithms. Their performance was analyzed using accuracy, precision, recall and confusion matrix.

## **Important Viva Questions**

**1. What is spam detection?**

Spam detection is the process of identifying unwanted or irrelevant emails and separating them from legitimate emails.

**2. What is binary classification?**

It is a classification technique in which data is divided into two classes.

**3. What is Ham?**

Ham refers to a normal or legitimate email that is not spam.

**4. What is TF-IDF?**

TF-IDF is a text feature extraction technique that converts text into numerical values based on word importance.

**5. What is a hyperplane?**

A hyperplane is a decision boundary used by SVM to separate different classes.

**6. What are support vectors?**

Support vectors are the data points closest to the decision boundary. They help determine the optimal hyperplane.

**7. What is the difference between KNN and SVM?**

KNN uses neighboring data points for classification, whereas SVM uses an optimal hyperplane to separate classes.

**8. Which algorithm is better for spam detection?**

SVM often performs better for text classification because it handles high-dimensional TF-IDF features effectively. However, the final choice should depend on actual evaluation results.

## **Practical Exam: What to Remember**

| Important Code           | Purpose                               |
| ------------------------ | ------------------------------------- |
| `TfidfVectorizer()`      | Converts text into numerical features |
| `train_test_split()`     | Divides training and testing data     |
| `KNeighborsClassifier()` | Creates KNN model                     |
| `SVC(kernel='linear')`   | Creates SVM model                     |
| `fit()`                  | Trains the model                      |
| `predict()`              | Predicts email category               |
| `accuracy_score()`       | Calculates accuracy                   |
| `confusion_matrix()`     | Evaluates classification              |
| `precision_score()`      | Calculates precision                  |
| `recall_score()`         | Calculates recall                     |

**One important dataset note:** This program assumes the common Kaggle SMS Spam Collection CSV format, with columns `v1` (label) and `v2` (message). If your college provides a differently named email dataset, the column names need to be adjusted. Also, for a rigorous evaluation, fit TF-IDF on training text only using a pipeline; the simplified code above fits it before splitting, which can cause data leakage.
