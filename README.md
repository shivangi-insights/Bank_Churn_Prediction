# Bank Customer Churn Prediction

## Project Overview

Customer churn is an important business challenge for retail banks because losing customers can negatively affect revenue stability, customer lifetime value, and future cross-selling opportunities.

This project develops a machine learning system to predict whether a bank customer is likely to churn based on demographic, account, and engagement-related characteristics.

The project applies classification techniques, evaluates model performance using multiple metrics, and translates machine learning outputs into business insights that can support customer retention strategies.

## Business Objective

The primary objective is to help banks identify customers who may be at higher risk of churn so that proactive retention strategies can be considered.

The model can support:

* Early identification of potentially at-risk customers
* Targeted customer retention campaigns
* Prioritization of retention efforts
* Personalized customer engagement
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

The project uses a **Decision Tree Classifier** for customer churn prediction.

The model was evaluated using:

* Accuracy
* ROC-AUC
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC Curve

The trained model and preprocessing pipeline are saved using Joblib for reuse.

## Model Performance

| Metric            | Result |
| ----------------- | -----: |
| Training Accuracy | 86.81% |
| Testing Accuracy  | 86.05% |
| Training AUC      | 0.8628 |
| Testing AUC       | 0.8402 |
| Precision         |   0.78 |
| Recall            |   0.44 |
| F1-Score          |   0.56 |

The testing ROC-AUC of **0.8402** indicates that the model demonstrates good ability to distinguish between customers who churn and customers who remain.

The relatively small difference between training and testing performance indicates reasonably consistent performance on unseen test data.

Because churn is a business problem where identifying actual churners is important, metrics such as recall and F1-score should also be considered alongside accuracy and ROC-AUC.

## Feature Importance

The Decision Tree identified the following features as the most influential in its predictions:

| Feature            | Importance |
| ------------------ | ---------: |
| Age                |     38.81% |
| Number of Products |     30.11% |
| Active Member      |     12.16% |
| Balance            |     10.68% |
| Germany            |      5.49% |

These values represent the features the trained Decision Tree relied on most when making predictions.

Feature importance indicates predictive contribution within this trained model and should not be interpreted as proof of causal relationships.

## Key Business Insights

The model's feature-importance analysis highlights several customer characteristics that were particularly influential in the model's churn predictions.

* **Age** was the most influential feature in the trained Decision Tree.
* **Number of Products** was another major contributor to model predictions.
* **Active Membership status** also had a meaningful contribution.
* **Account Balance** contributed to the model's predictions.
* **Geography**, particularly the Germany category, was also identified as an influential feature.

These findings can help guide further customer segmentation and retention analysis. They should be validated with additional business and customer-level analysis before being used to design retention strategies.

## Customer-Level Prediction

The project includes a customer-level prediction function that accepts individual customer information and returns:

* Predicted churn status
* Churn probability
* Risk level

### Example Output

```text
CUSTOMER CHURN PREDICTION
-----------------------------------
Prediction        : Likely to Churn
Churn Probability : 67.21%
Risk Level        : High
```

This demonstrates how the trained model can be used to generate an individual customer-level prediction.

## Business Application

A bank could use this type of system as a decision-support tool to identify customers who may require additional attention.

Potential applications include:

* Personalized retention offers
* Relationship-manager outreach
* Customer engagement campaigns
* Product recommendations
* Service-quality interventions
* Customer segmentation and prioritization

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
│   └── European_Bank.csv
│
├── models/
│   └── bank_churn_model.pkl
│
├── notebooks/
│   └── churn_analysis.ipynb
│
├── .gitignore
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
* Confusion matrix analysis
* Feature importance interpretation
* Customer churn prediction
* Business interpretation of machine learning results
* Python
* Scikit-learn
* Git/GitHub

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/shivangi-insights/Bank_Churn_Prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd Bank_Churn_Prediction
```

### 3. Create and Activate a Virtual Environment

On Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install the Required Libraries

```bash
pip install -r requirements.txt
```

### 5. Run the Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/churn_analysis.ipynb
```

and run the cells sequentially.

## Conclusion

This project demonstrates how machine learning can be applied to customer churn prediction in the banking sector.

The Decision Tree model achieved **86.05% testing accuracy** and a **0.8402 testing ROC-AUC**, providing a useful foundation for identifying customers who may be at higher risk of churn.

Beyond model development, the project demonstrates how predictive analytics can be translated into business insights that may support customer retention, segmentation, and relationship-management activities.

The model is intended as a decision-support tool and should be combined with appropriate business validation and customer-level analysis before deployment.
