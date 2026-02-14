<!-- please help me writemthe markdown  -->
# practicing hands-on Airflow
---

### what I learned:

- **DAG Authoring:** How to define and structure DAGs
- **Operators:** BashOperator, PythonOperator, and more
- **Task Dependencies:** Setting up task order and parallelism
- **XComs:** Passing data between tasks
- **Branching:** Conditional task execution
- **Scheduling:** Using presets, cron, and custom intervals
- **Asset Dependencies:** Managing dependencies between data assets
- **DAG Orchestration:** Parent/child DAG relationships

### How to run the code:

1. Run `docker-compose up` to start the Airflow environment.
2. Access the Airflow web UI at `http://localhost:8080`.
3. Use the default credentials (username: `airflow`, password: `airflow`) to log in.
4. Navigate to the "DAGs" tab to see the list of available DAGs.

> Note: Make sure to have Docker installed and running on your machine before executing the above command.

If the execution fails, try to run `docker compose restart` to restart the Airflow

