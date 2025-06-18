# This repo is my basic lesson about Airflow with Docker
First of all, you can learn from this before using this repo
https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html
## Requirements:
- Docker
- Python
- DBeaver or another tool to connect to PostgreSQL

## Let's Start:

1. Clone the repository:
   git clone <this_repo_url>
   cd Airflow-Docker

2. Build and start the containers:
sh ```
   make build
   make up
```
3. Check Docker Desktop to see the running containers.

4. Connect to PostgreSQL using DBeaver (check the `.env` file for connection info).

5. Access the Airflow UI at: http://localhost:8080
   - Username: airflow
   - Password: airflow

6. Ensure Airflow is connected to PostgreSQL.

7. Run and check your DAGs in the Airflow UI.
