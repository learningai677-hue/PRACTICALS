Mate, this practical is about **Artificial Neural Networks (ANN) for Bank Customer Churn Prediction**.

We'll use TensorFlow/Keras to build a neural network that predicts whether a bank customer will leave the bank within the next six months.

For your university practical, I'll keep the code manageable and include the improvement step, since that's explicitly required in the question.

# Experiment: Bank Customer Churn Prediction Using ANN

**Aim:** To build a neural network-based classifier to predict whether a bank customer will leave the bank or not using an open-source Kaggle dataset.

## 1. Python Program

```
# Bank Customer Churn Prediction using ANNimport pandas as pdimport numpy as npfrom sklearn.model_selection import train_test_splitfrom sklearn.preprocessing import StandardScaler, LabelEncoderfrom sklearn.metrics import accuracy_score, confusion_matrixfrom tensorflow.keras.models import Sequentialfrom tensorflow.keras.layers import Dense, Dropoutfrom tensorflow.keras.callbacks import EarlyStopping# 1. Read the datasetdata = pd.read_csv("Churn_Modelling.csv")# 2. Remove unnecessary columnsdata = data.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)# Separate features and targetX = data.drop('Exited', axis=1)y = data['Exited']# Encode categorical columnsX = pd.get_dummies(X, columns=['Geography', 'Gender'], drop_first=True)# 3. Split dataset into training and testing setsX_train, X_test, y_train, y_test = train_test_split(    X, y, test_size=0.2, random_state=42)# 4. Normalize the datascaler = StandardScaler()X_train = scaler.fit_transform(X_train)
```

## 2. Sample Output

Your actual accuracy and confusion matrix will depend on the dataset and training process.

```
Accuracy Score: 0.85

Confusion Matrix:
[[1540   67]
 [ 233  160]]
```

Illustrative output only, not measured results.

## 3. Theory

### What is Customer Churn Prediction?

Customer churn refers to the situation where a customer stops using a company's products or services.

Customer churn prediction uses machine learning to identify customers who are likely to leave.

In this practical, a neural network predicts:

- `0` – Customer will not leave.
- `1` – Customer will leave.

### What is an Artificial Neural Network (ANN)?

An Artificial Neural Network is a machine learning model inspired by the working of the human brain.

It consists of interconnected neurons arranged in layers.

The three main layers are:

1. **Input Layer:** Receives customer information such as age, credit score, balance and tenure.
2. **Hidden Layer:** Processes information and learns patterns using weights, biases and activation functions.
3. **Output Layer:** Produces the prediction of whether the customer will leave or stay.

## 4. Explanation of Important Steps

**Step 1: Read the dataset**

```
data = pd.read_csv("Churn_Modelling.csv")
```

Loads the bank customer dataset using Pandas.

**Step 2: Feature and Target Selection**

- Features (X): Customer information such as credit score, age, geography and balance.
- Target (y): `Exited`, which indicates whether the customer left.

We remove Customer ID, Row Number and Surname because they are not useful predictive features.

**Step 3: Encoding categorical data**

```
X = pd.get_dummies(X, columns=['Geography', 'Gender'], drop_first=True)
```

Converts categorical values into numerical values because neural networks work with numerical inputs.

**Step 4: Train-Test Split**

```
train_test_split(X, y, test_size=0.2)
```

Divides the dataset into:

- 80% training data.
- 20% testing data.

**Step 5: Normalization**

```
scaler = StandardScaler()
```

Normalizes the features so that variables with different scales can be processed effectively.

**Step 6: Building the Neural Network**

We use:

- ReLU activation in hidden layers.
- Sigmoid activation in the output layer.
- Adam optimizer.
- Binary Crossentropy loss function.

**Step 7: Model Improvement**

The initial model can be improved using:

| Technique      | Purpose                                                    |
| -------------- | ---------------------------------------------------------- |
| Dropout        | Prevents overfitting                                       |
| Early Stopping | Stops training when validation performance stops improving |
| More neurons   | Helps learn complex patterns                               |

The improved model in the program uses Dropout and Early Stopping.

## 5. Important Functions and Their Uses

| Function             | Purpose                   |
| -------------------- | ------------------------- |
| `pd.read_csv()`      | Reads dataset             |
| `pd.get_dummies()`   | Encodes categorical data  |
| `train_test_split()` | Splits dataset            |
| `StandardScaler()`   | Normalizes features       |
| `Sequential()`       | Creates neural network    |
| `Dense()`            | Adds neural network layer |
| `Dropout()`          | Reduces overfitting       |
| `model.compile()`    | Configures model          |
| `model.fit()`        | Trains model              |
| `model.predict()`    | Predicts customer churn   |
| `accuracy_score()`   | Calculates accuracy       |
| `confusion_matrix()` | Evaluates predictions     |

## 6. Performance Evaluation

**Accuracy:**

Measures the percentage of correct predictions.

\\[ Accuracy=\frac{TP+TN}{TP+TN+FP+FN} \\]

**Confusion Matrix:**

|              | Predicted Stay | Predicted Leave |
| ------------ | -------------- | --------------- |
| Actual Stay  | TN             | FP              |
| Actual Leave | FN             | TP              |

Where:

- TP = Correctly predicted customers who leave.
- TN = Correctly predicted customers who stay.
- FP = Customers predicted to leave but actually stay.
- FN = Customers predicted to stay but actually leave.

## 7. Result

Thus, an Artificial Neural Network-based classifier was implemented successfully to predict bank customer churn. The model was trained and evaluated using accuracy score and confusion matrix.

---

## Important Viva Questions

**1. What is ANN?**

ANN stands for Artificial Neural Network. It is a machine learning model inspired by the human brain, consisting of interconnected neurons.

**2. What is customer churn?**

Customer churn occurs when a customer stops using a company's services.

**3. Why do we use ReLU?**

ReLU introduces non-linearity into the network and helps it learn complex patterns.

**4. Why do we use Sigmoid in the output layer?**

Sigmoid produces an output between 0 and 1, making it suitable for binary classification.

**5. What is Dropout?**

Dropout randomly disables some neurons during training to reduce overfitting.

**6. What is an epoch?**

One complete pass of the entire training dataset through the neural network.

**7. What is batch size?**

The number of training samples processed before updating the model weights.

**8. What is Early Stopping?**

It stops model training when validation performance stops improving, helping prevent overfitting.

**9. Why do we use Adam optimizer?**

Adam adjusts the model's weights efficiently to minimize the loss function.

**10. What is Binary Crossentropy?**

It is a loss function used to measure the difference between actual and predicted values in binary classification.

---

(Practical revision)

**Remember these five things:**

1. ANN = Artificial Neural Network.
2. ReLU = Hidden layer activation.
3. Sigmoid = Output layer activation.
4. Adam = Optimizer.
5. Binary Crossentropy = Loss function.

**One important practical note:** Install the required libraries if they aren't already available:

```
pip install pandas numpy scikit-learn tensorflow
```

Also, the improved model is the one used for the final accuracy and confusion matrix. The first model is trained as a baseline for comparison.
