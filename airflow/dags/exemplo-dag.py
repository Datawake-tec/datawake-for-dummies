# Exemplo de DAG para testar o setup do Airflow
# Coloque este arquivo na pasta ./dags/

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# Argumentos padrão para a DAG
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definição da DAG
dag = DAG(
    'exemplo_dag_simples',
    default_args=default_args,
    description='DAG de exemplo para testar o Airflow standalone',
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=['exemplo', 'teste'],
)

# Função Python para ser executada como task
def imprimir_informacoes():
    print("Executando DAG de exemplo no Airflow!")
    print(f"Data e hora atual: {datetime.now()}")
    return "Task executada com sucesso!"

# Task 1: Executar comando bash
task_bash = BashOperator(
    task_id='executar_comando_bash',
    bash_command='echo "Olá do Airflow Standalone!" && date',
    dag=dag,
)

# Task 2: Executar função Python
task_python = PythonOperator(
    task_id='executar_funcao_python',
    python_callable=imprimir_informacoes,
    dag=dag,
)

# Task 3: Verificar status
task_status = BashOperator(
    task_id='verificar_status',
    bash_command='echo "Todas as tasks foram executadas com sucesso!"',
    dag=dag,
)

# Definir dependências entre as tasks
task_bash >> task_python >> task_status