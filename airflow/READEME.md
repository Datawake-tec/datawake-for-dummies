# Scripts de Inicialização do Airflow Standalone
# Instruções passo a passo para configurar e executar

## Pré-requisitos
- Docker e Docker Compose instalados
- Pelo menos 4GB de RAM disponível para o Docker

## Passo 1: Criar estrutura de diretórios
Crie as pastas necessárias na raiz do projeto:


## Passo 2: Inicializar e executar o Airflow
```bash
# Executar o container
docker compose up -d

# Verificar logs
docker compose logs -f airflow-standalone

# Verificar status
docker compose ps
```
## Passo 3 Acessar o Airflow
- URL: http://localhost:8080
- Usuário: admin
- Senha: admin

## Comandos úteis
```bash
# Parar os containers
docker compose down

# Parar e remover volumes
docker compose down -v

# Executar comandos do Airflow
docker compose exec airflow-standalone airflow version

# Listar DAGs
docker compose exec airflow-standalone airflow dags list

# Ver logs de uma DAG específica
docker compose exec airflow-standalone airflow tasks test exemplo_dag_simples executar_comando_bash 2024-01-01
```

## Estrutura de diretórios final
```
projeto/
├── docker-compose.yml
├── exemplo-dag.py (copiar para dags/)
├── dags/
│   └── exemplo-dag.py
├── logs/
├── plugins/
```

## Solução de problemas
1. Se o container não iniciar, verifique se há RAM suficiente
2. Se as DAGs não aparecerem, verifique as permissões dos arquivos
3. Para reiniciar completamente: `docker-compose down -v` e depois `docker-compose up -d`