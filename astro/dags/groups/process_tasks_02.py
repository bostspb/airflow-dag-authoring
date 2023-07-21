from airflow.decorators import task
from airflow.utils.task_group import TaskGroup


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


def process_tasks_02(partners_settings):
    with TaskGroup(group_id="process_tasks_02") as process_tasks:
        process_a(partners_settings['partner_name'], partners_settings['partner_path'])
        process_b(partners_settings['partner_name'], partners_settings['partner_path'])
        process_c(partners_settings['partner_name'], partners_settings['partner_path'])
    return process_tasks
