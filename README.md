## This repo is my basic code about Airflow with Docker
First of all, you can learn from this before using this repo

https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html

## What you can learn from this repos: 
- first_dag: Demonstrates the traditional way of building a DAG and  define dependencies between tasks manually.
- taskflow_dag: Demonstrates building a DAG using the TaskFlow API — a  readable approach.
- connect_postgres_dag:  interact with a PostgreSQL database in Airflow (make sure Airflow is connected to PostgreSQL first).
- postgres_hook_dag: Demonstrates how to use the PostgresHook in Airflow to execute queries or retrieve data from a PostgreSQL database.

## Requirements:
- Docker
- Python
- DBeaver or another tool to connect to PostgreSQL

## Let's Start:

1. Clone the repository:
```sh
   git clone <this_repo_url>
   cd Airflow-Docker
```
2. create this fold and grant write permissions to them 
```sh
    mkdir -p data logs plugins dags
    chmod -R 777 dags logs plugins data

    ```

```
3. Build and start the containers:
 ```sh
   make build
   make up
```
4. Check Docker Desktop to see the running containers.

5. Connect to PostgreSQL using DBeaver (check the `.env` file for connection info).

6. Access the Airflow UI at: http://localhost:8080
   - Username: airflow
   - Password: airflow

7. Ensure Airflow is connected to PostgreSQL.

8. Run and check your DAGs in the Airflow UI.

### Happy coding!
