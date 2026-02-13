from airflow.sdk import dag, task

@dag(
     dag_id="xcoms_dag_kwargs",
)
def xcoms_dag_kwargs():
    @task.python
    def first_task(**kwargs):
        # Extracted `ti` (task instance) from kwargs to push XCom manually
        ti = kwargs['ti']
        print("Extracting data... This is the first task")
        fetched_data = {"data": [1, 2, 3, 4, 5]}
        ti.xcom_push(key='return_result', value=fetched_data)
    
    @task.python
    def second_task(**kwargs):
        ti = kwargs['ti']
        # pulling XCom pushed by the first task
        fetched_data = ti.xcom_pull(key='return_result', task_ids='first_task')['data']
        print("Transforming data... This is the second task")
        transformed_data = fetched_data * 2
        transformed_data_dict = {"transformed_data": transformed_data}
        ti.xcom_push(key='return_result', value=transformed_data_dict)

    @task.python
    def third_task(**kwargs):
        ti = kwargs['ti']
        load_data = ti.xcom_pull(key='return_result', task_ids='second_task')
        return load_data

    #  defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

# Instantiate the DAG
xcoms_dag_kwargs()