from airflow.sdk import dag, task
import os

@dag(
     dag_id="second_dag_orchestrate",
)
def second_dag_orchestrate():
    @task.python
    def first_task():
        print("This is the first task")
    
    @task.python
    def second_task():
        print("This is the second task")

    @task.python
    def third_task():
        os.makedirs(os.path.dirname("/opt/airflow/logs/data"), exist_ok=True)

        # write the content to the file
        with open("/opt/airflow/logs/data/output_2.txt", 'w') as f:
            f.write(f"Data extracted successfully !!!\n")

    #  defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

# Instantiate the DAG
second_dag_orchestrate()