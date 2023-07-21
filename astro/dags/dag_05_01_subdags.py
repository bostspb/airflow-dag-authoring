from datetime import datetime
from airflow.decorators import task, dag
from airflow.operators.subdag import SubDagOperator
from subdag.subdag_factory import subdag_factory


@task.python(task_id="extract_partners", do_xcom_push=False, multiple_outputs=True)
def extract():
    partner_name = "netflix"
    partner_path = "/partners/netflix"
    return {"partner_name": partner_name, "partner_path": partner_path}


default_args = {
    "start_date": datetime(2023, 7, 20)
}


@dag(description="DAG is charge of processing customer data",
     default_args=default_args,
     schedule_interval=None,
     tags=["data_science", "test"],
     catchup=False,
     max_active_runs=1)
def dag_05_01_subdags():
    process_tasks = SubDagOperator(
        task_id="process_tasks",
        subdag=subdag_factory("dag_05_01_subdags", "process_tasks", default_args)
    )
    extract() >> process_tasks


dag_05_01_subdags()
