# Airflow pipeline example 

In this tutorial we will use Airflow to implement a simple regression pipeline. Note that this is just meant as a demonstration of how to set up a simple pipeline and is not an example of a realistic machine learning pipeline in production.

The simple pipeline will include three tasks:

1) data preprocessing using pandas (task output: csv-file), 
2) model building with scikit-learn (task output: trained model object)
3) model prediction (task output: csv-file with prediction)


- First you need to install Airflow: [Installation tutorial](https://kirenz.github.io/codelabs/codelabs/airflow-setup/#0) 

- Copy the content of this repo on your machine.
- Save `reg_dag_happy.py` in your home folder `~/airflow/dags`
- Create a new folder in `dags`. Call it `dag_reg_example`
- Save all other scripts in `~/airflow/dags/dag_reg_example` 

Now follow the steps explained in this [installation tutorial](https://kirenz.github.io/codelabs/codelabs/airflow-setup/#0)  starting from step 7 "First pipeline". Just replace the names of the taks and files.
