# The Astronomer Certification: Apache Airflow DAG Authoring Preparation Course
> https://academy.astronomer.io/astronomer-certification-apache-airflow-dag-authoring-preparation

## 1. Welcome!
  - 1.1 Introduction
  - 1.2 Installing Docker
  - 1.3 [Installing the Astro CLI](01_03_installing_the_astro_cli.md)    
  - 1.4 [Running airflow 2.0 with the Astro CLI](01_04_running_airflow.md)

## 2. The Basics
  - 2.1 Define your DAG: the right way
  - 2.2 [DAG Scheduling 101](02_02_dag_scheduling.md)
  - 2.3 [Cron vs Timedelta](02_03_cron_vs_timedelta.md)
  - 2.4 Task idempotence and determinism
  - 2.5 [Backfilling](02_05_backfilling.md)

## 3. [Master your Variables](astro/dags/dag_03_master_your_variables.py)
  - 3.1 Variables
  - 3.2 Properly fetch your Variables
  - 3.3 The Power of Environment Variables
  - 3.4 A Few Additional Notes

## 4. The power of the TaskFlow API
  - 4.1 [Add data at runtime with templating](astro/dags/dag_04_01_add_data_at_runtime_with_templating.py)
  - 4.2 [Sharing data with XCOMs and limitations](astro/dags/dag_04_02_sharing_data_with_xcoms.py)
  - 4.3 [The new way of creating DAGs](astro/dags/dag_04_03_new_way_of_creating_dags.py)
  - 4.4 [XComs with the TaskFlow API](astro/dags/dag_04_04_xcoms_with_the_taskflow_api.py)

## 5. Grouping your tasks
  - 5.1 [SubDAGs: The Hard Way of Grouping your Tasks](astro/dags/dag_05_01_subdags.py)
  - 5.2 [TaskGroups: The Best Way of Grouping your Tasks](astro/dags/dag_05_02_taskgroups.py)

## 6. Advanced Concepts
  - 6.1  [The (not so) dynamic tasks](astro/dags/dag_06_01_dynamic_tasks.py)
  - 6.2  [Make your choices with Branching](astro/dags/dag_06_02_branching.py)
  - 6.3  Change task execution with Trigger Rules
  - 6.4  [Dependencies and Helpers](astro/dags/dag_06_04_dependencies_and_helpers.py)
  - 6.5  [Get the control of your tasks](astro/dags/dag_06_05_control_tasks.py)
  - 6.6  [Dealing with resource consuming tasks with Pools](astro/dags/dag_06_06_pools.py)
  - 6.7  [Execute critical tasks first, the others after](astro/dags/dag_06_07_task_priority.py)
  - 6.8  [What if a task needs the output of its previous execution?](astro/dags/dag_06_08_depending_on_past.py)
  - 6.9  Demystifying wait for downstream
  - 6.10 [All you need to know about Sensors](astro/dags/dag_06_10_sensors.py)
  - 6.11 [Don't get stuck with your Tasks by using Timeouts](astro/dags/dag_06_11_timeouts.py)
  - 6.12 [How to react in case of failure? or retry?](astro/dags/dag_06_12_callbacks.py)
  - 6.13 [The different (and smart) ways of retrying your tasks](astro/dags/dag_06_13_task_retries.py)
  - 6.14 [Get notified with SLAs](astro/dags/dag_06_14_sla.py)
  - 6.15 [DAG versioning](astro/dags/dag_06_15_dags_versioning.py)
  - 6.16 [Dynamic DAGs: The two ways!](astro/dags/dag_06_16_dynamic_dags.py)

## 7. DAG dependencies
  - 7.1 [Wait for multiple DAGs with the ExternalTaskSensor](astro/dags/dag_07_01_external_task_sensor.py)
  - 7.2 [DAG dependencies with the TriggerDagRunOperator](astro/dags/dag_07_02_trigger_dag_run_operator.py)

## 8. Well done!
  - 8.1 Quick message for you!
