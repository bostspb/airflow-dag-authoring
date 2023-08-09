import time
from datetime import datetime
from airflow.decorators import task, dag
from airflow.operators.empty import EmptyOperator


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
    "start_date": datetime(2023, 7, 20),
    "retries": 0  # !!!
}


@dag(description="DAG is charge of processing customer data",
     default_args=default_args,
     schedule_interval=None,
     tags=["data_science", "test"],
     catchup=False,
     max_active_runs=1)
def dag_06_08_depending_on_past():
    start = EmptyOperator(task_id="start")
    storing = EmptyOperator(task_id="storing", trigger_rule="none_failed")

    for partner, details in partners.items():
        @task.python(
            task_id=f"extract_{partner}",
            do_xcom_push=False,
            multiple_outputs=True,
            depends_on_past=True  # !!!
        )
        def extract(partner_name, partner_path):
            time.sleep(2)
            # raise ValueError("failed")
            return {"partner_name": partner_name, "partner_path": partner_path}

        extracted_values = extract(details['name'], details['path'])
        start >> extracted_values
        process(extracted_values["partner_name"], extracted_values["partner_path"]) >> storing


dag_06_08_depending_on_past()
