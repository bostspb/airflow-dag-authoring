from datetime import datetime
from airflow.decorators import task, dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator


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


def _choosing_partner_based_on_day(execution_date):
    day = execution_date.day_of_week
    if day == 1:
        return 'extract_partner_snowflake'
    if day == 3:
        return 'extract_partner_netflix'
    if day == 5:
        return 'extract_partner_astronomer'
    else:
        return 'stop'


@dag(description="DAG is charge of processing customer data",
     default_args=default_args,
     schedule_interval=None,
     tags=["data_science", "test"],
     catchup=False,
     max_active_runs=1)
def dag_06_02_branching():
    start = EmptyOperator(task_id="start")

    choosing_partner_based_on_day = BranchPythonOperator(
        task_id="choosing_partner_based_on_day",
        python_callable=_choosing_partner_based_on_day
    )

    stop = EmptyOperator(task_id="stop")
    storing = EmptyOperator(task_id="storing", trigger_rule="none_failed")
    choosing_partner_based_on_day >> stop

    for partner, details in partners.items():
        @task.python(task_id=f"extract_{partner}", do_xcom_push=False, multiple_outputs=True)
        def extract(partner_name, partner_path):
            return {"partner_name": partner_name, "partner_path": partner_path}

        extracted_values = extract(details['name'], details['path'])
        start >> choosing_partner_based_on_day >> extracted_values
        process(extracted_values["partner_name"], extracted_values["partner_path"]) >> storing


dag_06_02_branching()
