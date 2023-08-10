import time
from datetime import datetime, timedelta
from airflow.decorators import task, dag
from airflow.operators.empty import EmptyOperator
from airflow.exceptions import AirflowTaskTimeout, AirflowSensorTimeout


partners = {
    "partner_snowflake": {
        "name": "snowflake",
        "path": "/partners/snowflake"
    },
    "partner_netflix": {
        "name": "netflix",
        "path": "/partners/netflix"
    },
    "partner_astronomer": {
        "name": "astronomer",
        "path": "/partners/astronomer"
    }
}


@task.python
def process(partner_name, partner_path):
    print(partner_name)
    print(partner_path)


default_args = {
    "start_date": datetime(2023, 7, 20)
}


def _success_callback(context):
    print(context)


def _failure_callback(context):
    print(context)


def _extract_callback_success(context):
    print('SUCCESS CALLBACK')


def _extract_callback_failure(context):
    if context['exception']:
        if isinstance(context['exception'], AirflowTaskTimeout):
            print('FAILURE CALLBACK: AirflowTaskTimeout')
        if isinstance(context['exception'], AirflowSensorTimeout):
            print('FAILURE CALLBACK: AirflowSensorTimeout')
    print('FAILURE CALLBACK')


def _extract_callback_retry(context):
    if context['ti'].try_number() > 2:
        pass
    print('RETRY CALLBACK')


@dag(description="DAG is charge of processing customer data",
     default_args=default_args,
     schedule_interval=None,
     tags=["data_science", "test"],
     catchup=False,
     max_active_runs=1,
     on_success_callback=_success_callback,  # !!!
     on_failure_callback=_failure_callback   # !!!
     )
def dag_06_12_callbacks():
    start = EmptyOperator(
        task_id="start",
        execution_timeout=timedelta(minutes=10)
    )

    storing = EmptyOperator(task_id="storing", trigger_rule="none_failed")

    for partner, details in partners.items():
        @task.python(
            task_id=f"extract_{partner}",
            do_xcom_push=False,
            multiple_outputs=True,
            on_success_callback=_extract_callback_success,  # !!!
            on_failure_callback=_extract_callback_failure,  # !!!
            on_retry_callback=_extract_callback_retry       # !!!
        )
        def extract(partner_name, partner_path):
            time.sleep(2)
            return {"partner_name": partner_name, "partner_path": partner_path}

        extracted_values = extract(details['name'], details['path'])
        start >> extracted_values
        process(extracted_values["partner_name"], extracted_values["partner_path"]) >> storing


dag_06_12_callbacks()
