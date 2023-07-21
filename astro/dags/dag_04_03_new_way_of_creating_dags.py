from datetime import datetime
from airflow.decorators import task, dag


@task.python
def extract():
    partner_name = "netflix"
    partner_path = "/partners/netflix"
    return {"partner_name": partner_name, "partner_path": partner_path}


@task.python
def process(partner_settings):
    print(partner_settings["partner_name"])


@dag(description="DAG is charge of processing customer data",
     start_date=datetime(2023, 7, 20),
     schedule_interval=None,
     tags=["data_science", "test"],
     catchup=False,
     max_active_runs=1)
def dag_04_03_new_way_of_creating_dags():
    process(extract())


dag_04_03_new_way_of_creating_dags()
