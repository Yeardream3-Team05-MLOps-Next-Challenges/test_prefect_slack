FROM prefecthq/prefect:2.18.3-python3.10

# Define build-time variable
ARG PREFECT_API_URL

ENV PREFECT_API_URL=$PREFECT_API_URL

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY flows /opt/prefect/flows

WORKDIR /opt/prefect/flows

CMD ["python", "flow.py"]