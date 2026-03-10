from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "luis",
    "retries": 2,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id="pipeline_data_lake",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args
) as dag:

    airbyte_ingestion = BashOperator(
        task_id="airbyte_ingestion",
        bash_command="python3 /opt/airflow/scripts/trigger_airbyte.py"
    )

    spark_transformation = BashOperator(
        task_id="spark_transformation",
        bash_command="python3 /opt/airflow/scripts/spark_transform.py"
    )

    move_to_gold = BashOperator(
        task_id="move_to_gold",
        bash_command="python3 /opt/airflow/scripts/move_to_gold.py"
    )

    airbyte_ingestion >> spark_transformation >> move_to_gold