Automobile Price Prediction System
End-to-End Machine Learning Pipeline with Flask Deployment

This project demonstrates the complete lifecycle of a production-ready Machine Learning system — from raw data ingestion and statistical analysis to model optimization and web deployment.

The application predicts automobile prices using advanced regression techniques and a fully engineered preprocessing pipeline.

***Business Objective***

Accurately estimate car prices based on technical specifications and categorical attributes to support:

- Pricing strategy decisions

- Automotive market analysis

- Valuation automation systems

📊 Dataset

Source: UCI Machine Learning Repository

Dataset: Automobile Imports (1985)

Target Variable: price

The dataset contains both numeric and categorical features, making it ideal for demonstrating real-world ML preprocessing challenges.

- Technical Highlights
✔ Advanced Data Cleaning

Missing value handling (custom replacement + imputation)

Type conversion and coercion

Duplicate detection

Target-based filtering

✔ Statistical Feature Analysis

- Pearson Correlation (linear relationships)

- Spearman Correlation (non-linear & robust to outliers)

- Kruskal-Wallis Test (categorical vs numeric impact)

- Chi-Square Test (categorical dependency analysis)

This demonstrates strong statistical reasoning beyond basic EDA.

*****Machine Learning Architecture*****
****Preprocessing Strategy (Production-Level)****

Implemented using ColumnTransformer + Pipeline:

- RobustScaler → Outlier-sensitive features

- MinMaxScaler → Bounded variables

- StandardScaler → Normally distributed features

- OneHotEncoder → Categorical variables

- Automated imputation within pipeline

✔ Fully reproducible
✔ Prevents data leakage
✔ Cross-validation safe

****Models Implemented****

- Linear Regression

- Polynomial Regression

- Ridge Regression

- Lasso Regression

- Polynomial Ridge

- Polynomial Lasso

****Model Selection & Optimization****

10-Fold Cross Validation

RMSE evaluation

GridSearchCV for hyperparameter tuning

Regularization comparison to reduce overfitting

Final model serialized using joblib.

****Evaluation Metric****

Primary Metric: Root Mean Squared Error (RMSE)

Used both for:

Cross-validation performance

Test set evaluation

This ensures reliable generalization performance.
Deployment

The best-performing model is deployed using Flask.

****Project Structure****
├── app.py                # Flask application
├── price_model.pkl       # Serialized trained model
├── requirements.txt
├── README.md
├── templates/
│   └── index.html        # Web form interface

Users input automobile features via a web form, and the trained ML model returns predicted price in real-time.

****Tech Stack****

- Python

- NumPy

- Pandas

- Scikit-learn

- SciPy

- Matplotlib & Seaborn

- Flask

- Joblib
