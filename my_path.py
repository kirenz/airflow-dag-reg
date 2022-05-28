""" 
    Define path variables

"""

from pathlib import Path

# Obtain home path
home_path = str(Path.home())
# Define path to your airflow/dags/etc
airflow_path = "/airflow/dags/dag_reg_example/"
