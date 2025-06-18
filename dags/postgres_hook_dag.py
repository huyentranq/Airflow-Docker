from datetime import datetime, timedelta
import pendulum
import  os 

from airflow import DAG
from airflow.decorators import task 
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
# from airflow.providers.postgres.operators.sql import SQLExecuteQueryOperator

default_args ={
    'owner': 'trang',
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id ="load_employ_local",
    default_args= default_args,
    schedule_interval="@daily",
    start_date = pendulum.datetime(2024,1,1),
    catchup = False 
    
) as dag:
    create_employee_table = PostgresOperator(
        task_id = "create_employee_table",
        postgres_conn_id="postgres_localhost",
        sql="""
            CREATE TABLE IF NOT EXISTS employees(
                "Id" NUMERIC PRIMARY KEY,
                "Company Name" TEXT,
                "Employee Markme" TEXT
            )
        """,
        
        )
        
    create_employees_temp_table = PostgresOperator(
            task_id="create_employees_temp_table",
            postgres_conn_id="postgres_localhost",
            sql="""
                DROP TABLE IF EXISTS employees_temp;
                CREATE TABLE employees_temp (
                    "Id" NUMERIC PRIMARY KEY,
                    "Company Name" TEXT,
                    "Employee Markme" TEXT
                );
            """,
            )
            
    @task()
    def load_csv_to_temp_table():
        data_path = "/opt/airflow/data/employees.csv"
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"file not exist: {data_path}")
            
        postgres_hook = PostgresHook(postgres_conn_id="postgres_localhost")
        conn = postgres_hook.get_conn()
        cur = conn.cursor()
        
        with open(data_path,"r") as file:
                cur.copy_expert(
                "COPY employees_temp FROM STDIN WITH CSV HEADER DELIMITER AS ',' QUOTE '\"'",
                file,
            )
        conn.commit()

    @task()
    def merge_data():
        query = """
            INSERT INTO employees
            SELECT *
            FROM (
                SELECT DISTINCT *
                FROM employees_temp
            ) t
            ON CONFLICT ("Id") DO UPDATE
            SET
                "Employee Markme" = excluded."Employee Markme",
                "Company Name" = excluded."Company Name";
        """
        postgres_hook = PostgresHook(postgres_conn_id="postgres_localhost")
        conn = postgres_hook.get_conn()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()

    # Thiết lập luồng
    [create_employee_table, create_employees_temp_table] >> load_csv_to_temp_table() >> merge_data()


    
    
    
    
    










