#  Retail Data Pipeline WITH AIRFLOW POSTGRES DBT SODA

## Objective
The goal of this project is to create an end-to-end data pipeline from a Kaggle dataset on retail data. This involves modeling the data into fact-dimension tables, implementing data quality steps, utilizing modern data stack technologies (dbt, Soda, and Airflow), and storing the data in Postgres The project is containerized via Docker and versioned on GitHub.
- Data Ingestion: We’ll start by extracting data from a CSV file and loading it into a PostgreSQL database, instead of snowflake.
- Quality Checks: Using Soda, we’ll perform data quality checks to ensure data integrity and completeness.
- Data Transformation: We’ll use dbt (Data Build Tool) to transform the raw data into structured, analysis-ready data models.
- Orchestration: Apache Airflow will be used to automate and manage our data workflows, ensuring smooth and timely execution.

# 🌟 System Architecture
![image](https://github.com/user-attachments/assets/c8f8ef68-063a-487e-a65b-aef19b17cfb6)


# 📁 Repository Structure
```shell
├── dags
│ ├── creation_table_country.sql
│ ├── postgres_ingest_data.py
├── include
│ ├── dataset
│ │ └── online_retail.csv
│ ├── dbt
│ │ ├── dbt_packages
│ │ ├── models
│ │ │ ├── report
│ │ │ ├── sources
│ │ │ └── transform
│ │ ├── cosmos_config.py
│ │ ├── dbt_project.yml
│ │ ├── packages.yml
│ │ └── profiles.yml
│ ├── soda
│ │ ├── checks
│ │ │ ├── report
│ │ │ ├── sources
│ │ │ └── transform
│ │ ├── check_function.py
│ │ └── configuration.yml
├── logs
├── plugins
├── .env
├── airflow.cfg
├── docker-compose.yml
└── Dockerfile
```

## Data modeling
![image](https://github.com/user-attachments/assets/c4b5421f-84ad-42bd-9edf-103b642034f0)

## 🚀 Getting Started
1.  **Clone the repository**:

    ```bash
    git clone https://github.com/FA3001/ELT-pipeline
    ```
2.  **Launch Docker**
    ```bash
    docker-compose up -d
    ```
3. **Download Data**
   ```bash
    /include/datasets/online_retail.csv
   ```
4. **API key for Soda Cloud**
   Create an account on soda.io and generating the API key and it's associated secret, put them in
   ```bash
    include/soda/configuration.yml
   ```
5. **Initialize DBT configuration within the scheduler**
   ```bash
   docker ps
   docker exec -it <scheduler_container_name or scheduler_container_id> bash
    ```
6. **Activate the dbt_venv**
   ```bash
    source dbt_venv/bin/activate
   ```
7. **Go to include/dbt**
      ```bash
    cd include/dbt
   ```
8. **Install DBT dependencies**
   ```bash
    dbt deps
   ```
9. **Access Airflow UI**: **Uesername and Pass: airflow**
   ```bash
    http://localhost:8080/
   ```
   
