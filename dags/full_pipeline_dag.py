from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.python import PythonOperator
from scripts.create_external_schema import create_external_schema
from scripts.metabase_automation import create_metabase_dashboard


default_args = {
    "start_date": datetime(2024, 1, 1)
}

with DAG("dob_batch_pipeline",
         schedule_interval="@daily",
         default_args=default_args,
         catchup=False) as dag:

    run_dlt = BashOperator(
        task_id="run_dlt_ingestion",
        bash_command="cd /opt/airflow/job-dlt-pipeline && python rest_api_pipeline.py"
    )

    run_glue = BashOperator(
        task_id='run_glue_crawler',
        bash_command='cd /opt/airflow/scripts && python run_glue_crawler.py',
        dag=dag
    )
    
    
    create_external_schema_task = PythonOperator(
        task_id="create_external_schema",
        python_callable=create_external_schema,
        dag=dag,
    )


    copy_to_redshift = BashOperator(
        task_id="query_spectrum_to_table",
        bash_command="cd /opt/airflow/scripts && python copy_to_redshift.py",
        dag=dag
    )

    run_dbt = BashOperator(
        task_id="run_dbt_transform",
        bash_command="cd /opt/airflow/dags/dob_dbt_project && dbt run --profiles-dir /opt/airflow/dags",
        dag=dag,
    )

    run_dbt_test = BashOperator(
        task_id="run_dbt_test",
        bash_command="cd /opt/airflow/dags/dob_dbt_project && dbt test --profiles-dir /opt/airflow/dags"
    )
    
    
    run_metabase = PythonOperator(
        task_id='create_metabase_dashboard',
        python_callable=create_metabase_dashboard
    )
    

    run_dlt >> run_glue >>  create_external_schema_task >> copy_to_redshift >> run_dbt >> run_dbt_test >> run_metabase