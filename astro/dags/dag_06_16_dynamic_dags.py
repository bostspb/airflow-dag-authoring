from airflow import DAG
from airflow.decorators import task
from datetime import datetime

partners = {
    'snowflake': {
        'schedule': '@daily',
        'path': '/data/snowflake'
    },
    'netflix': {
        'schedule': '@weekly',
        'path': '/data/netflix'
    },
}


"""
------------------------
 The Single-File Method
------------------------

== Drawbacks with this method ==
1) DAGs are generated every time the Scheduler parses the DAG folder (If you have a lot of DAGs to generate, 
   you may experience performance issues
2) There is no way to see the code of the generated DAG on the UI
3) If you change the number of generated DAGs, you will end up with DAGs visible on the UI that no longer exist 
"""


def generate_dag(dag_id, schedule_interval, details, default_args):
    with DAG(dag_id, schedule_interval=schedule_interval, default_args=default_args) as dag:
        @task.python
        def process(path):
            print(f'Processing: {path}')

        process(details['path'])

    return dag


for partner, details in partners.items():
    dag_id = f'dag_06_16_dynamic_dag_{partner}'
    default_args = {
        'start_date': datetime(2021, 1, 1)
    }
    globals()[dag_id] = generate_dag(dag_id, details['schedule'], details, default_args)


"""
------------------------
 The Multi-File Method
------------------------

== Steps: ==
1) Create a template file corresponding to your DAG structure with the different tasks. In it, for the inputs, you put some placeholders that the script will use to replace with the actual values.
2) Create a python script in charge of generating the DAGs by creating a file and replacing the placeholders in your template file with the actual values.
3) Put the script, somewhere else than in the folder DAGs.
4) Trigger this script either manually or with your CI/CD pipeline.

== The pros of this method: ==
- It is Scalable as DAGs are not generated each time the folder dags/ is parsed by the Scheduler
- Full visibility of the DAG code (one DAG -> one file)
- Full control over the way DAGs are generated (script, less prone to errors or "zombie" DAGs)
"""
