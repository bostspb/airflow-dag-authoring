from datetime import datetime
from airflow.decorators import task, dag
from airflow.utils.task_group import TaskGroup
from groups.process_tasks_02 import process_tasks_02


@task.python(task_id="extract_partners", do_xcom_push=False, multiple_outputs=True)
def extract():
    partner_name = "netflix"
    partner_path = "/partners/netflix"
    return {"partner_name": partner_name, "partner_path": partner_path}


@task.python
def process_a(partner_name, partner_path):
    print(partner_name)
    print(partner_path)


@task.python
def process_b(partner_name, partner_path):
    print(partner_name)
    print(partner_path)


@task.python
def process_c(partner_name, partner_path):
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
def dag_05_02_taskgroups():
    partners_settings = extract()
    with TaskGroup(group_id="process_tasks_01") as process_tasks_01:
        process_a(partners_settings['partner_name'], partners_settings['partner_path'])
        process_b(partners_settings['partner_name'], partners_settings['partner_path'])
        process_c(partners_settings['partner_name'], partners_settings['partner_path'])

    process_tasks_02(partners_settings)


dag_05_02_taskgroups()
