# -*- coding: utf-8 -*-
"""
    Regression model

Step 1) Import data
Step 2) Prepara data
Step 3) Fit model
Step 4) Store model

"""
#------------------------------------------------------
# Setup
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from joblib import dump

from my_path import home_path, airflow_path

#------------------------------------------------------
# Step 1) Import data 
df = pd.read_csv(home_path + airflow_path + "df_prepped.csv")

#------------------------------------------------------
# Step 2) Prepare data
# Select features for simple regression
X = df[['gdp_per_capita']]
# Create response
y = df["life_satisfaction"]
# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#------------------------------------------------------
# Step 3) Fit model
# Select regression model
reg = LinearRegression()
# Train the model
reg.fit(X_train, y_train)

#------------------------------------------------------
# Step 4) Store model
dump(reg, home_path + airflow_path + 'my_linear_model.joblib')