from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator


def _extract_01(ti):
    partner_name = "netflix"
    ti.xcom_push(key="partner_name", value=partner_name)


def _process_01(ti):
    partner_name = ti.xcom_pull(key="partner_name", task_ids="extract_01")
    print(partner_name)


def _extract_02():
    partner_name = "netflix"
    return partner_name


def _process_02(ti):
    partner_name = ti.xcom_pull(task_ids="extract_02")
    print(partner_name)


def _extract_03():
    partner_name = "netflix"
    partner_path = "/partners/netflix"
    return {"partner_name": partner_name, "partner_path": partner_path}


def _process_03(ti):
    partner_settings = ti.xcom_pull(task_ids="extract_03")
    print(partner_settings['partner_name'])


with DAG(dag_id="dag_04_02_sharing_data_with_xcoms",
         description="DAG is charge of processing customer data",
         start_date=datetime(2023, 7, 20),
         schedule_interval=None,
         tags=["data_science", "test"],
         catchup=False,
         max_active_runs=1) as dag:
    extract_01 = PythonOperator(
        task_id="extract_01",
        python_callable=_extract_01
    )

    process_01 = PythonOperator(
        task_id="process_01",
        python_callable=_process_01
    )

    extract_01 >> process_01

    extract_02 = PythonOperator(
        task_id="extract_02",
        python_callable=_extract_02
    )

    process_02 = PythonOperator(
        task_id="process_02",
        python_callable=_process_02
    )

    extract_02 >> process_02

    extract_03 = PythonOperator(
        task_id="extract_03",
        python_callable=_extract_03
    )

    process_03 = PythonOperator(
        task_id="process_03",
        python_callable=_process_03
    )

    extract_03 >> process_03
