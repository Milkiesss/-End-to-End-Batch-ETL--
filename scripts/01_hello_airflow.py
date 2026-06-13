from airflow import DAG  # импортируем класс DAG для создания directed acyclic graph
from airflow.operators.python import PythonOperator  # импортируем оператор для выполнения Python функций
from datetime import datetime  # импортируем datetime для работы с датами и временем

def hello_world():  # определяем функцию, которая будет выполняться в Airflow
    print("Hello, Airflow!")  
    return "succes"  

with DAG(  # создаем контекстный менеджер для DAG
    dag_id="hello_airflow",  # уникальный идентификатор нашего DAG
    start_date=datetime(2026, 1, 1),  # дата начала запуска DAG
    schedule_interval=None,  # интервал запуска (None = ручной запуск)
    catchup=False,  # не запускать задачи за прошлые периоды
) as dag:  # присваиваем DAG переменной dag
        task1 = PythonOperator(  # создаем задачу типа PythonOperator
            task_id="hello_world_task",  # уникальный идентификатор задачи
            python_callable=hello_world,  # указываем функцию для выполнения
        )  # закрываем определение оператора