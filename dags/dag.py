from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 14),
    'retries': 1,
}

with DAG('dbt_transform', default_args=default_args, schedule_interval=None) as dag:
    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='docker exec dbt bash -c "cd /usr/app/dbt && dbt seed"'
    )

    run_dbt