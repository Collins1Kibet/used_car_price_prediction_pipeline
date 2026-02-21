**Automobile Price Prediction System**

A Machine Learning web application that predicts car prices using multiple regression models.

The model is trained on the UCI Automobile Dataset and deployed using Flask as a web interface.

***Project Overview***

This project:

- Loads and cleans the UCI Automobile dataset

- Performs Exploratory Data Analysis (EDA)

- Applies statistical tests (Pearson, Spearman, Kruskal, Chi-Square)

- Builds preprocessing pipelines using ColumnTransformer

- Trains multiple regression models:

- Linear Regression

- Polynomial Regression

- Ridge Regression

- Lasso Regression

- Polynomial + Ridge

- Polynomial + Lasso

- Uses Cross-Validation & GridSearchCV for model tuning

- Selects the best-performing model

- Saves the final model using joblib

- Deploys the trained model using Flask

***Dataset***

Source: UCI Machine Learning Repository
Dataset: Automobile Imports 1985 Dataset

The dataset contains car features such as:

- Engine size

- Horsepower

- Wheel base

- Fuel type

- Body style

- Curb weight

- City MPG / Highway MPG

- And more...

Target variable: price

***Machine Learning Pipeline***
1. Data Cleaning

- Replaced missing values (?) with NaN

- Converted numeric columns

- Dropped rows with missing target values

2. Statistical Analysis

- Pearson Correlation

- Spearman Correlation

- Kruskal-Wallis Test (categorical vs numeric)

- Chi-square test (categorical vs categorical)

3. Feature Engineering & Preprocessing

- Different scalers were applied strategically:

- RobustScaler → for outlier-sensitive features

- MinMaxScaler → bounded features

- StandardScaler → normally distributed features

- OneHotEncoder → categorical variables

Implemented using:
- ColumnTransformer
- Pipeline

***Models Implemented***

- Linear Regression

- Polynomial Regression

- Ridge Regression

- Lasso Regression

- Polynomial Ridge

- Polynomial Lasso

Model selection performed using:

- 10-Fold Cross Validation

- RMSE evaluation

- GridSearchCV for hyperparameter tuning
