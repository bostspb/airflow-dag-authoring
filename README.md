# The Astronomer Certification: Apache Airflow DAG Authoring Preparation Course
> https://academy.astronomer.io/astronomer-certification-apache-airflow-dag-authoring-preparation

## Welcome!
  - Introduction
  - Installing Docker
  - [Installing the Astro CLI](01_03_installing_the_astro_cli.md)    
  - [Running airflow 2.0 with the Astro CLI](01_04_running_airflow.md)

## The Basics
  - Define your DAG: the right way
  - [DAG Scheduling 101](02_02_dag_scheduling.md)
  - [Cron vs Timedelta](02_03_cron_vs_timedelta.md)
  - Task idempotence and determinism
  - [Backfilling](02_05_backfilling.md)

## [Master your Variables](astro/dags/dag_03_master_your_variables.py)
  - Variables
  - Properly fetch your Variables
  - The Power of Environment Variables
  - A Few Additional Notes

## The power of the TaskFlow API
  - [Add data at runtime with templating](astro/dags/dag_04_01_add_data_at_runtime_with_templating.py)
  - [Sharing data with XCOMs and limitations](astro/dags/dag_04_02_sharing_data_with_xcoms.py)
  - [The new way of creating DAGs](astro/dags/dag_04_03_new_way_of_creating_dags.py)
  - [XComs with the TaskFlow API](astro/dags/dag_04_04_xcoms_with_the_taskflow_api.py)

## Grouping your tasks
  - [SubDAGs: The Hard Way of Grouping your Tasks](astro/dags/dag_05_01_subdags.py)
  - [TaskGroups: The Best Way of Grouping your Tasks](astro/dags/dag_05_02_taskgroups.py)

## Advanced Concepts
  - [The (not so) dynamic tasks](astro/dags/dag_06_01_dynamic_tasks.py)
  - [Make your choices with Branching](astro/dags/dag_06_02_branching.py)
  - Change task execution with Trigger Rules
  - [Dependencies and Helpers](astro/dags/dag_06_04_dependencies_and_helpers.py)
  - [Get the control of your tasks](astro/dags/dag_06_05_control_tasks.py)
  - [Dealing with resource consuming tasks with Pools](astro/dags/dag_06_06_pools.py)
  - [Execute critical tasks first, the others after](astro/dags/dag_06_07_task_priority.py)
  - [What if a task needs the output of its previous execution?](astro/dags/dag_06_08_depending_on_past.py)
  - Demystifying wait for downstream
  - All you need to know about Sensors
  - Don't get stuck with your Tasks by using Timeouts
  - How to react in case of failure? or retry?
  - The different (and smart) ways of retrying your tasks
  - Get notified with SLAs
  - DAG versioning
  - Dynamic DAGs: The two ways!

## DAG dependencies
  - Wait for multiple DAGs with the ExternalTaskSensor
  - DAG dependencies with the TriggerDagRunOperator

## Well done!
  - Quick message for you!
