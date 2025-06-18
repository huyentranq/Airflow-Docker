from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'my_name',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='first_dag',
    default_args=default_args,
    description='This is my first DAG',
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo "this is my first task and I will run first! "'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command= 'echo "this is sencond task "'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command= 'echo "this is third task "'
    )

    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # Task dependency method 3
    task1 >> [task2, task3]