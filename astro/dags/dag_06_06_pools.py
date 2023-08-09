from datetime import datetime
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator
import time


default_args = {
    "start_date": datetime(2023, 7, 20)
}


@dag(description="DAG is charge of processing customer data",
     default_args=default_args,
     schedule_interval=None,
     tags=["data_science", "test"],
     catchup=False)
def dag_06_06_pools():
    t1 = EmptyOperator(task_id="t1")
    t2 = EmptyOperator(task_id="t2")
    t1 >> t2

    t3 = EmptyOperator(task_id="t3")
    t4 = EmptyOperator(task_id="t4")
    t5 = EmptyOperator(task_id="t5")

    # Одновременно будет выполняться только одна таска из трех,
    # т.к. мы привязали ее к отдельному пулу `partner_pool`, где выставили в GUI всего один слот
    for i in [1, 2, 3]:
        @task.python(task_id=f"dummy_{i}", pool="partner_pool")
        def dummy():
            time.sleep(2)

        dummy_task = dummy()
        t2 >> dummy_task >> t3

    # process_tasks = SubDagOperator(
    #     task_id="process_tasks",
    #     subdag=subdag_factory(...),
    #     pool="partner_pool"
    # )

    # You can configure the number of slots occupied by a task by updating the pool_slots parameter (the default is 1).
    # Modifying this value could be useful in cases where you are using pools to manage resource utilization.
    for i in [1, 2, 3]:
        @task.python(task_id=f"funny_{i}", pool_slots=3)
        def funny():
            time.sleep(2)

        funny_task = funny()
        t3 >> funny_task >> t4

    t4 >> t5


dag_06_06_pools()
