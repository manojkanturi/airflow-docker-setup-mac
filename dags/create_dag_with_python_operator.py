from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta



default_args = {
    'owner': 'mani',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_name():
    #print(f"Hello World ! My name is {name},"
     #     f"and I am {age} years old! ")
    return 'Jerry'

with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v03',
    description='our first dag using pyhon operator',
    start_date=datetime(2023, 10, 6),
    schedule_interval='@daily'
) as dag:
    
    #task1 = PythonOperator(
    #        task_id='greet',
    #       python_callable=greet,
    #        op_kwargs={'name':'Mani', 'age':26}
    #)

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

   # task1
    task2