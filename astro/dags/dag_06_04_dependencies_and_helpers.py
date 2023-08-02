from datetime import datetime
from airflow.decorators import task, dag
from airflow.operators.empty import EmptyOperator
from airflow.models.baseoperator import cross_downstream, chain


default_args = {
    "start_date": datetime(2023, 7, 20)
}


@dag(description="DAG is charge of processing customer data",
     default_args=default_args,
     schedule_interval=None,
     tags=["data_science", "test"],
     catchup=False,
     max_active_runs=1)
def dag_06_04_dependencies_and_helpers():
    """
    Cross Downstream
    """
    t1 = EmptyOperator(task_id="t1")
    t2 = EmptyOperator(task_id="t2")
    t3 = EmptyOperator(task_id="t3")
    t4 = EmptyOperator(task_id="t4")
    t5 = EmptyOperator(task_id="t5")
    t6 = EmptyOperator(task_id="t6")
    t7 = EmptyOperator(task_id="t7")

    # `[t1, t2, t3] >> [t4, t5, t6]` - doesn't work, should use next one:
    cross_downstream([t1, t2, t3], [t4, t5, t6])
    [t4, t5, t6] >> t7

    """   
    Chain
    """
    w1 = EmptyOperator(task_id="w1")
    w2 = EmptyOperator(task_id="w2")
    w3 = EmptyOperator(task_id="w3")
    w4 = EmptyOperator(task_id="w4")
    w5 = EmptyOperator(task_id="w5")
    w6 = EmptyOperator(task_id="w6")

    chain(w1, [w2, w3], [w4, w5], w6)

    """   
    Mixing Cross Downstream with Chain
    """
    m1 = EmptyOperator(task_id="m1")
    m2 = EmptyOperator(task_id="m2")
    m3 = EmptyOperator(task_id="m3")
    m4 = EmptyOperator(task_id="m4")
    m5 = EmptyOperator(task_id="m5")
    m6 = EmptyOperator(task_id="m6")

    cross_downstream([m2, m3], [m4, m5])
    chain(m1, m2, m5, m6)


dag_06_04_dependencies_and_helpers()
