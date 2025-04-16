from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.producer import run_producer
from scripts.consumer import run_consumer


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 14),
    'retries': 1,
}

with DAG(dag_id='supply_chain_pipeline',default_args=default_args,schedule_interval='@hourly',catchup=False) as dag:

    # run_dbt = BashOperator(task_id='run_dbt', bash_command='docker exec dbt bash -c "cd /usr/app/dbt && dbt seed"')

    producer = PythonOperator(task_id='producer', python_callable=run_producer)
    consumer = PythonOperator(task_id='consumer', python_callable=run_consumer)

    [producer,consumer]
