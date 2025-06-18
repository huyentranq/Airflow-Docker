from datetime import datetime, timedelta

from airflow.decorators import dag, task


default_args = {
    'owner': 'my_name',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='taskflow_dag', 
     default_args=default_args, 
     start_date=datetime(2021, 10, 26), 
     schedule_interval='@daily',
     catchup = False
     
     )
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_infor():
        return {
            'name': 'James',
            'age': 15,
            'city': 'Hanoi'
        }

    @task()
    def get_school():
        return 'Coder2J Academy'

    @task()
    def hello_world(name, age,city, school):
        print(f"My name is {name}, I live in {city},  and I am {age} years old!")
        print(f"I am studying this lesson from {school}.")
    
    my_infor = get_infor()
    school = get_school()
    hello_world(name = my_infor['name'],
                 city = my_infor['city'],
                 school = school,
                 age = my_infor['age']
)

greet_dag = hello_world_etl()