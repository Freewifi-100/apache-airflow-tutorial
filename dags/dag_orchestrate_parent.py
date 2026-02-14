from dag_orchestrate_1 import first_dag_orchestrate
from dag_orchestrate_2 import second_dag_orchestrate
from airflow.sdk import dag, task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

@dag(
        dag_id="dag_orchestrate_parent",
)

def dag_orchestrate_parent():
    trigger_first_dag = TriggerDagRunOperator(
        task_id="trigger_first_dag",
        trigger_dag_id="first_dag_orchestrate",
        wait_for_completion=True,  # Wait for the first DAG to complete before triggering the second DAG
    )

    trigger_second_dag = TriggerDagRunOperator(
        task_id="trigger_second_dag",
        trigger_dag_id="second_dag_orchestrate",
        wait_for_completion=True,  # Wait for the second DAG to complete before finishing the parent DAG
    )

    trigger_first_dag >> trigger_second_dag

# Instantiate the DAG
dag_orchestrate_parent()