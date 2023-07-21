from datetime import datetime
from airflow.decorators import task, dag
from typing import Dict


@task.python(task_id="extract_partners_01", multiple_outputs=True)
def extract_01():
    partner_name = "netflix"
    partner_path = "/partners/netflix"
    return {"partner_name": partner_name, "partner_path": partner_path}
    # XCom will be:
    # return_value ->	{'partner_name': 'netflix', 'partner_path': '/partners/netflix'}
    # partner_path ->	/partners/netflix
    # partner_name ->	netflix


@task.python
def process_01(partner_settings):
    print(partner_settings["partner_name"])


@task.python(task_id="extract_partners_02")
def extract_02() -> Dict[str, str]:
    partner_name = "netflix"
    partner_path = "/partners/netflix"
    return {"partner_name": partner_name, "partner_path": partner_path}
    # XCom will be the same as in extract_01()


@task.python
def process_02(partner_settings):
    print(partner_settings["partner_name"])


@task.python(task_id="extract_partners_03", do_xcom_push=False, multiple_outputs=True)
def extract_03():
    partner_name = "netflix"
    partner_path = "/partners/netflix"
    return {"partner_name": partner_name, "partner_path": partner_path}
    # XCom will be:
    # partner_path ->	/partners/netflix
    # partner_name ->	netflix


@task.python
def process_03(partner_name, partner_path):
    print(partner_name)
    print(partner_path)


@dag(description="DAG is charge of processing customer data",
     start_date=datetime(2023, 7, 20),
     schedule_interval=None,
     tags=["data_science", "test"],
     catchup=False,
     max_active_runs=1)
def dag_04_04_xcoms_with_the_taskflow_api():
    process_01(extract_01())

    process_02(extract_02())

    partners_settings = extract_03()
    process_03(partners_settings['partner_name'], partners_settings['partner_path'])


dag_04_04_xcoms_with_the_taskflow_api()
