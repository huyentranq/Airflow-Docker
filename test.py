from datetime imort datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'code2j',
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}


@dag(dag_id ='dag_with_bash_operator_v01',
     default_args=default_args,
     start_date=datetime(2023, 10, 1),
     schedule_interval='@daily',
     catchup=False)

def hello_world():
    @task(multiple_output =True)
    def get_name():
        return {
            'first_name': 'John',
            'last_name': 'Doe'
        }
    
    @task()
    def get_age():
        return 30
    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World! My name is {first_name} {last_name} "
              f"and I am {age} years old!")
        

    name_dict = get_name()
    age = get_age()
    greet(first_name= name_dict['first_name'],
          last_name =name_dict['first_name'],
          age = age)
greet_dag = hello_world()