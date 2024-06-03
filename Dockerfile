FROM prefecthq/prefect:2.18.3-python3.10

# Define build-time variable
#ARG PREFECT_API_URL
ARG SLACK_WEBHOOK

#ENV PREFECT_API_URL=$PREFECT_API_URL
ENV SLACK_WEBHOOK=$SLACK_WEBHOOK

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /opt/prefect/flows

WORKDIR /opt/prefect/flows

CMD ["python", "flow.py"]