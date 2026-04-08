# Automobile Price Prediction System

## Project Overview
This project is a machine learning application that predicts automobile prices based on vehicle features. It leverages **Scikit-learn pipelines**, **cross-validation**, and **GridSearchCV** for model selection and hyperparameter tuning. The final model is deployed as a **Flask web application** for real-time predictions.

The goal is to provide an end-to-end solution—from data preprocessing and model building to deployment—demonstrating practical skills in data science and machine learning.

---

## Tools & Technologies
- Python (Pandas, NumPy, Scikit-learn)
- Machine Learning Pipelines (ColumnTransformer, Pipeline)
- Cross-validation (K-Fold)
- Hyperparameter tuning (GridSearchCV)
- Flask for web deployment
- Joblib for model serialization
- Data Visualization (Matplotlib, Seaborn)

---

## Project Workflow

### 1. Data Loading & Cleaning
- Loaded automobile dataset from [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/automobile)
- Assigned proper column names and converted numeric fields
- Handled missing values, outliers, and data inconsistencies

### 2. Exploratory Data Analysis (EDA)
- Visualized distributions of numeric features
- Checked skewness and correlations with the target (`price`)
- Applied statistical tests for categorical vs numeric relationships (Kruskal-Wallis, Chi-square)
- Identified important features influencing price

### 3. Feature Engineering & Pipelines
- Defined numeric and categorical feature groups
- Built **ColumnTransformer pipelines** for preprocessing:
  - RobustScaler, MinMaxScaler, StandardScaler for numeric features
  - OneHotEncoder for categorical features
- Supported polynomial feature expansion for advanced models

### 4. Model Training & Evaluation
- Tested multiple regression models:
  - Linear Regression
  - Polynomial Regression
  - Ridge, Lasso
  - Polynomial Ridge, Polynomial Lasso
- Applied 10-fold cross-validation for robust evaluation
- Hyperparameter tuning using **GridSearchCV**
- Evaluated models using RMSE on both CV and test sets

### 5. Model Deployment
- Best model (`PolynomialRidge`) serialized using **Joblib**
- Flask app (`app.py`) allows users to input vehicle features and get real-time price predictions
- Web interface built with **HTML templates** for a clean, responsive UI

---

## 📁 Project Structure

* ├── app.py # Flask application for deployment
* ├── auto_price_model.pkl # Original trained model
* ├── price_model.pkl # Final model used in Flask app
* ├── requirements.txt # Python dependencies
* ├── used_car_price_prediction.ipynb # Jupyter notebook with full EDA & modeling workflow
* └── README.md # Project documentation

---

## 📊 Key Features
- End-to-end ML pipeline from raw data to deployment
- Handles missing values and feature scaling automatically
- Supports multiple regression models with cross-validation
- Hyperparameter tuning for optimal performance
- Real-time price prediction via web interface

---

## 🔑 Model Performance
- Best Model: Polynomial Ridge Regression
- Cross-Validation RMSE: 2618.78
- Test RMSE: 2973.24
- Captures nonlinear relationships between car features and price effectively

---

## 📌 Future Improvements
- Integrate a front-end framework (React, Bootstrap) for enhanced UI
- Support batch predictions from CSV uploads
- Implement model retraining with new data
- Deploy to a cloud service (Heroku, AWS, or Azure)
