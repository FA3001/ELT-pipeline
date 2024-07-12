FROM apache/airflow:2.8.0

RUN python -m venv soda_venv && \
    . soda_venv/bin/activate && \
    export PIP_USER=false && \
    pip install --upgrade pip && \
    pip install -i https://pypi.cloud.soda.io soda-postgres && \
    pip install pendulum && \
    pip install soda-core-scientific==3.0.45 && \
    deactivate

RUN python -m venv dbt_venv && \
    . dbt_venv/bin/activate && \
    export PIP_USER=false && \
    pip install --upgrade pip && \
    pip install dbt-postgres && \
    pip install protobuf==3.20.0 && \
    deactivate

RUN pip install astronomer-cosmos