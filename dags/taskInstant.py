from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'my_name',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

@dag(
    dag_id="xcom_with_context_example",
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False
)
def xcom_demo():

    @task
    def push_data():
        from airflow.operators.python import get_current_context
        ti = get_current_context()['ti']
        result = 5 + 7
        ti.xcom_push(key="sum_result", value=result)
        print(f"[PUSH] Tổng là: {result}")

    @task
    def pull_data(next_ds):
        from airflow.operators.python import get_current_context
        ti = get_current_context()['ti']
        value = ti.xcom_pull(task_ids="push_data", key="sum_result")
        print(f"[PULL] Kết quả từ XCom là: {value}")
        print(f"[INFO] Ngày chạy kế tiếp (next_ds): {next_ds}")

    result_task = push_data()
    pull_data(result_task)

dag_instance = xcom_demo()