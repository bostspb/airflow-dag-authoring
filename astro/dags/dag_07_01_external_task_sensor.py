from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.empty import EmptyOperator
from airflow.sensors.external_task import ExternalTaskSensor

with DAG(dag_id="dag_07_01_external_task_sensor",
         description="DAG is charge of processing customer data",
         start_date=datetime(2023, 7, 20),
         schedule_interval="@daily",
         dagrun_timeout=timedelta(minutes=10),
         tags=["data_science", "test"],
         catchup=False,
         max_active_runs=1) as dag:

    waiting_for_task = ExternalTaskSensor(
        task_id="waiting_for_task",
        external_dag_id="dag_06_12_callbacks",
        external_task_id="storing",
        # execution_delta=
        # execution_date_fn=
        failed_states=['failed', 'skipped'],
        allowed_states=['success']
    )

    cleaning_xcoms = EmptyOperator(task_id="cleaning_xcoms")

    waiting_for_task >> cleaning_xcoms

