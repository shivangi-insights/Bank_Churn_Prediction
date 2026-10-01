# Bank Customer Churn Prediction

## Project Overview

Customer churn is an important business challenge for retail banks because losing customers can negatively affect revenue stability, customer lifetime value, and future cross-selling opportunities.

This project develops a machine learning system to predict whether a bank customer is likely to churn based on demographic, account, and engagement-related characteristics.

The project uses classification algorithms and evaluates their ability to identify customers at higher risk of leaving the bank.

## Business Objective

The primary objective is to help banks identify customers who may be at higher risk of churn so that proactive retention strategies can be considered.

The model can support:

* Early identification of potentially at-risk customers
* Targeted customer retention campaigns
* Personalized customer engagement
* Prioritization of retention efforts
* Data-driven customer relationship management

## Dataset

The dataset contains customer-level information including:

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Account Balance
* Number of Products
* Credit Card ownership
* Active Membership status
* Estimated Salary
* Churn status

The target variable is `Exited`, where:

* `0` = Customer stayed
* `1` = Customer churned

## Project Workflow

The project follows a standard machine learning workflow:

1. Data loading and inspection
2. Exploratory data analysis
3. Data preprocessing
4. Train-test split
5. Feature transformation
6. Model training
7. Model evaluation
8. ROC-AUC analysis
9. Confusion matrix analysis
10. Feature importance analysis
11. Customer-level churn prediction
12. Business interpretation

## Machine Learning Model

The final model used for prediction is a **Decision Tree Classifier**.

The model was evaluated using:

* Accuracy
* ROC-AUC
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC Curve

## Final Model Performance

| Metric            | Result |
| ----------------- | -----: |
| Training Accuracy | 86.81% |
| Testing Accuracy  | 86.05% |
| Training AUC      | 0.8628 |
| Testing AUC       | 0.8402 |
| Precision         |   0.78 |
| Recall            |   0.44 |
| F1-Score          |   0.56 |

The testing ROC-AUC of **0.8402** indicates that the model has good ability to distinguish between customers who churn and customers who remain.

## Feature Importance

The Decision Tree identified the following features as the most influential in its predictions:

| Feature            | Importance |
| ------------------ | ---------: |
| Age                |     38.81% |
| Number of Products |     30.11% |
| Active Member      |     12.16% |
| Balance            |     10.68% |
| Germany            |      5.49% |

These values represent the features the trained Decision Tree relied on most when making predictions. They should not be interpreted as proof of causal relationships.

## Customer Prediction

The project also includes a customer-level prediction function that accepts individual customer information and returns:

* Predicted churn status
* Churn probability
* Risk level

Example output:

```text
CUSTOMER CHURN PREDICTION
-----------------------------------
Prediction        : Likely to Stay
Churn Probability : 9.00%
Risk Level        : Low
```

## Business Application

A bank could use this type of system as a decision-support tool to identify customers who may require additional attention.

Potential actions could include:

* Personalized retention offers
* Relationship-manager outreach
* Customer engagement campaigns
* Product recommendations
* Service-quality interventions

The model should support business decision-making rather than serve as the sole basis for customer decisions.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook
* Joblib
* Git / GitHub

## Project Structure

```text
Bank_Churn_Prediction/
│
├── data/
├── notebooks/
│   └── bank_churn_prediction.ipynb
│
├── src/
├── models/
├── README.md
└── requirements.txt
```

## Skills Demonstrated

This project demonstrates practical skills in:

* Data preprocessing
* Exploratory data analysis
* Feature engineering and transformation
* Classification modeling
* Model evaluation
* ROC-AUC analysis
* Feature importance interpretation
* Customer churn prediction
* Business interpretation of machine learning results
* Python
* Scikit-learn
* Git/GitHub

## Conclusion

The project demonstrates how machine learning can be applied to customer churn prediction in the banking sector.

The final Decision Tree model achieved **86.05% testing accuracy** and a **0.8402 testing ROC-AUC**, providing a useful foundation for identifying customers who may be at higher risk of churn and supporting proactive retention strategies.
