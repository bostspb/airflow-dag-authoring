import time
from datetime import datetime
from airflow.decorators import task, dag
from airflow.operators.empty import EmptyOperator
from airflow.sensors.date_time import DateTimeSensor


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


@dag(description="DAG is charge of processing customer data",
     default_args=default_args,
     schedule_interval=None,
     tags=["data_science", "test"],
     catchup=False,
     max_active_runs=1)
def dag_06_10_sensors():
    start = EmptyOperator(task_id="start")

    delay = DateTimeSensor(
        task_id="delay",
        target_time="{{ execution_date.add(hours=9) }}",
        poke_interval=60 * 60,
        mode="reschedule",
        timeout=60 * 60 * 10,
        # execution_timeout=60,
        soft_fail=True,  # -> state 'skipped'
        exponential_backoff=True
    )
    start >> delay

    storing = EmptyOperator(task_id="storing", trigger_rule="none_failed")

    for partner, details in partners.items():
        @task.python(task_id=f"extract_{partner}", do_xcom_push=False, multiple_outputs=True)
        def extract(partner_name, partner_path):
            time.sleep(2)
            return {"partner_name": partner_name, "partner_path": partner_path}

        extracted_values = extract(details['name'], details['path'])
        delay >> extracted_values
        process(extracted_values["partner_name"], extracted_values["partner_path"]) >> storing


dag_06_10_sensors()
