""" 
    Data preparation

Step 1) Import data with pandas
Step 2) Make some data corrections
Step 3) Save data as csv to local folder

"""
#------------------------------------------------------
# Setup
import pandas as pd
from pathlib import Path

from my_path import home_path, airflow_path

#------------------------------------------------------
# Step 1: Import data from GitHub
LINK = "https://raw.githubusercontent.com/kirenz/datasets/master/oecd_gdp.csv"
df = pd.read_csv(LINK)

#------------------------------------------------------
# Step 2: Change column names 
df.columns = df.columns.str.lower().str.replace(' ', '_')
#------------------------------------------------------

# Step 3: Save data to current working directory
df.to_csv(home_path + airflow_path + 'df_prepped.csv', index=False)