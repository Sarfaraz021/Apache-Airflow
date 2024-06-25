from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# Define the DAG
with DAG(dag_id="first_pipeline", start_date=datetime(2023, 1, 1), schedule_interval="@daily") as dag:

    # Define tasks
    start_task = BashOperator(
        task_id='start',
        bash_command='echo "Starting the pipeline..."'
    )

    @task
    def process_data():
        print("Processing data...")

    end_task = BashOperator(
        task_id='end',
        bash_command='echo "Pipeline finished."'
    )

    # Set task dependencies
    start_task >> process_data() >> end_task
