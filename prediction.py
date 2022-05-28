"""
    Make prediction

Step 1) Import model 
Step 2) Create new data
Step 3) Make prediction
Step 4) Store prediction

"""
#------------------------------------------------------
# Setup
import pandas as pd
from joblib import load

from my_path import home_path, airflow_path

#------------------------------------------------------
# Step 1) Import model 
reg = load(home_path + airflow_path + 'my_linear_model.joblib')

#------------------------------------------------------
# Step 2) Make new data

# Create a new GDP value
X_new = pd.DataFrame({"gdp_per_capita": [50000]})

#------------------------------------------------------
# Step 3) Make prediction

# Make prediction
my_prediction = reg.predict(X_new)

#------------------------------------------------------
# Step 4) Save prediction

# Save prediction as dataframe 
df_prediction = pd.DataFrame({"pred": my_prediction})

# Store predictions as csv
df_prediction.to_csv(home_path + airflow_path + "my_prediction.csv", echo=False)

#------------------------------------------------------