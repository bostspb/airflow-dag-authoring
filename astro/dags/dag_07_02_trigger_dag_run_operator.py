from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.empty import EmptyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG(dag_id="dag_07_01_external_task_sensor",
         description="DAG is charge of processing customer data",
         start_date=datetime(2023, 7, 20),
         schedule_interval="@daily",
         dagrun_timeout=timedelta(minutes=10),
         tags=["data_science", "test"],
         catchup=False,
         max_active_runs=1) as dag:

    cleaning_xcoms = EmptyOperator(task_id="cleaning_xcoms")

    trigger_other_dag = TriggerDagRunOperator(
        task_id="trigger_other_dag",
        trigger_dag_id="dag_06_14_sla",
        execution_date='{{ ds }}',
        wait_for_completion=True,
        poke_interval=60,
        reset_dag_run=True,
        failed_states=['failed']
    )

    cleaning_xcoms >> trigger_other_dag

