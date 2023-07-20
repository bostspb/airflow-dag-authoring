from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.models import Variable


def _extract_01():
    partner = Variable.get("my_dag_partner")
    print(partner)

    partner = Variable.get("my_dag_partner_secret")  # keyword "secret" hidden  it in UI and Logs the value
    print(partner)
    # airflow tasks test my_dag extract 2023-07-20


def _extract_02():
    partner = Variable.get("my_dag_partner_settings", deserialize_json=True)
    name = partner["name"]
    print(name)


def _extract_03(name):
    print(name)


with DAG("my_dag",
         description="DAG is charge of processing customer data",
         start_date=datetime(2023, 7, 20),
         schedule_interval="@daily",
         dagrun_timeout=timedelta(minutes=10),
         tags=["data_science", "test"],
         catchup=False,
         max_active_runs=1) as dag:

    extract_01 = PythonOperator(
        task_id="extract_01",
        python_callable=_extract_01
    )

    extract_02 = PythonOperator(
        task_id="extract_02",
        python_callable=_extract_02
    )

    extract_03 = PythonOperator(
        task_id="extract_03",
        python_callable=_extract_03,
        op_args=["{{ var.json.my_dag_partner_settings.name }}"]
    )

    extract_04 = PythonOperator(
        task_id="extract_04",
        python_callable=_extract_03,
        op_args=["{{ var.json.my_dag_partner_settings_from_env.name }}"]
    )
