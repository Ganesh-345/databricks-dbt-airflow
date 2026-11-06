from pendulum import datetime
from airflow.decorators import dag
from airflow.operators.bash import BashOperator

@dag(
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["dbt", "databricks"],
)
def databricks_dbt_workflow():

    run_dbt = BashOperator(
        task_id="dbt_run",
        bash_command="cd /usr/local/airflow/databricks_transformation && dbt run --profiles-dir .",
    )

    test_dbt = BashOperator(
        task_id="dbt_test",
        bash_command="cd /usr/local/airflow/databricks_transformation && dbt test --profiles-dir .",
    )

    run_dbt >> test_dbt

dag_instance = databricks_dbt_workflow()vfrom pendulum import datetime
from airflow.decorators import dag
from airflow.operators.bash import BashOperator

@dag(
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["dbt", "databricks"],
)
def databricks_dbt_workflow():

    run_dbt = BashOperator(
        task_id="dbt_run",
        bash_command="cd /usr/local/airflow/databricks_transformation && dbt run --profiles-dir .",
    )

    test_dbt = BashOperator(
        task_id="dbt_test",
        bash_command="cd /usr/local/airflow/databricks_transformation && dbt test --profiles-dir .",
    )

    run_dbt >> test_dbt

dag_instance = databricks_dbt_workflow()