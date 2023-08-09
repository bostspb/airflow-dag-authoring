from datetime import datetime
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


default_args = {
    "start_date": datetime(2023, 7, 20)
}

"""
------------
airflow.cfg:
------------
# The maximum number of task instances that can run concurrently per scheduler in Airflow.
parallelism = 32  

# The maximum number of task instances allowed to run concurrently in each DAG.
# Configurable at the DAG level with `concurrency` (since 2.2 -> `max_active_tasks`)
dag_concurrency = 16  # since 2.2 -> max_active_tasks_per_dag

# The maximum number of active DAG runs per DAG.
# Configurable at the DAG level with `max_active_runs`
max_active_runs_per_dag = 16

"""


@dag(description="DAG is charge of processing customer data",
     default_args=default_args,
     schedule_interval=None,
     tags=["data_science", "test"],
     catchup=False,
     max_active_runs=1,  # redefine `max_active_runs_per_dag` from airflow.cfg
     max_active_tasks=4  # redefine `max_active_tasks_per_dag` from airflow.cfg
     )
def dag_06_05_control_tasks():
    t1 = EmptyOperator(
        task_id="t1",
        task_concurrency=1  # that limits the number of active tasks through all DAG runs
    )
    t2 = EmptyOperator(task_id="t2")
    t1 >> t2


dag_06_05_control_tasks()
