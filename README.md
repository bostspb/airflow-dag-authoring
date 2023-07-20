# The Astronomer Certification: Apache Airflow DAG Authoring Preparation Course
> https://academy.astronomer.io/astronomer-certification-apache-airflow-dag-authoring-preparation

## Welcome!
  - Introduction
  - Installing Docker
  - [Installing the Astro CLI](01_03_installing_the_astro_cli.md)    
  - [Running airflow 2.0 with the Astro CLI](01_04_running_airflow.md)

## The Basics
  - Define your DAG: the right way
  - DAG Scheduling 101
  - Cron vs Timedelta
  - Task idempotence and determinism
  - Backfilling

## Master your Variables
  - Variables
  - Properly fetch your Variables
  - The Power of Environment Variables
  - A Few Additional Notes

## The power of the TaskFlow API
  - Add data at runtime with templating
  - Sharing data with XCOMs and limitations
  - The new way of creating DAGs
  - XComs with the TaskFlow API

## Grouping your tasks
  - SubDAGs: The Hard Way of Grouping your Tasks
  - TaskGroups: The Best Way of Grouping your Tasks

## Advanced Concepts
  - The (not so) dynamic tasks
  - Make your choices with Branching
  - Change task execution with Trigger Rules
  - Dependencies and Helpers
  - Get the control of your tasks
  - Dealing with resource consuming tasks with Pools
  - Execute critical tasks first, the others after
  - What if a task needs the output of its previous execution?
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
