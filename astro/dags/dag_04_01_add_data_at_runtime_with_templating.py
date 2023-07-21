from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator


class CustomPostgresOperator(PostgresOperator):
    template_fields = ('sql', 'parameters')


with DAG(dag_id="dag_04_01_add_data_at_runtime_with_templating",
         description="DAG is charge of processing customer data",
         start_date=datetime(2023, 7, 20),
         schedule_interval="@daily",
         dagrun_timeout=timedelta(minutes=10),
         tags=["data_science", "test"],
         catchup=False,
         max_active_runs=1) as dag:

    fetching_data_01 = PostgresOperator(
        task_id="fetching_data_01",
        sql="SELECT partner_name FROM partners WHERE date = {{ ds }}"
    )

    fetching_data_02 = PostgresOperator(
        task_id="fetching_data_02",
        sql="sql/my_request.sql"
    )

    fetching_data_03 = CustomPostgresOperator(
        task_id="fetching_data_03",
        sql="sql/my_request.sql",
        parameters={
            'next_ds': '{{ next_ds }}',
            'prev_ds': '{{ prev_ds }}',
            'partner_name': '{{ var.json.my_dag_partner_settings.name }}'
        }
    )
