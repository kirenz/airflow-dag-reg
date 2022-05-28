#---------------------------------------
# SETUP

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

# Module for manipulating dates and times
from datetime import datetime, timedelta

    # To change timezones, use Pendulum https://pendulum.eustace.io/

# Some convenience functions
from textwrap import dedent

#---------------------------------------
# DEFAULT DAG ARGUMENTS

with DAG(
    # the following string is the unique identifier for your DAG
    'dag_reg_example', 
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': True,
        'email': ['my-email@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2022, 6, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
    description='A simple regression DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=['example'],

) as dag:

    #---------------------------------------
    # DEFINE OPERATERS
    # t1, t2 and t3 are examples of tasks created by instantiating operators
    # they all will use the default_args we defined above
    
    t1 = BashOperator(
        depends_on_past=False,
        task_id='data_prep',
        bash_command='python /jankirenz/airflow/dags/dag_reg_example/data.py',
    )

    # Task documentation
    t1.doc_md = dedent(
        """\
    #### Task Documentation
    
    Data preparation

    """
    )

    #----------------

    t2 = BashOperator(
        task_id='model',
        depends_on_past=True,
        bash_command='python /jankirenz/airflow/dags/dag_reg_example/model.py',
    )

    #----------------
    
    t3 = BashOperator(
        task_id='prediction',
        depends_on_past=True,
        bash_command= 'python /jankirenz/airflow/dags/dag_reg_example/prediction.py',
    )

    #----------------
    # SETTING UP DEPENDENCIES 
    # We have tasks t1, t2 and t3 that do depend on each other. 

    t1 >> t2 >> t3