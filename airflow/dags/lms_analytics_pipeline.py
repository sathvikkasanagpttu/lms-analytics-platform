from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def extract():
    print("Extract: capture OLTP snapshots and telemetry into Bronze.")

def transform():
    print("Transform: run dbt staging and Gold dimensional models.")

def quality():
    print("Quality: validate uniqueness, not-null keys, accepted status values.")

def publish():
    print("Publish: refresh BI semantic layer and LMS analytics API cache.")

with DAG(
    dag_id="lms_analytics_daily",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={"retries": 2, "retry_delay": timedelta(minutes=5)},
    tags=["lms", "analytics", "elt"],
) as dag:
    t1 = PythonOperator(task_id="extract_bronze", python_callable=extract)
    t2 = PythonOperator(task_id="transform_gold", python_callable=transform)
    t3 = PythonOperator(task_id="data_quality", python_callable=quality)
    t4 = PythonOperator(task_id="publish_metrics", python_callable=publish)
    t1 >> t2 >> t3 >> t4
