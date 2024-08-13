FROM prefecthq/prefect:2.18.3-python3.10

ARG SLACK_WEBHOOK

ENV SLACK_WEBHOOK=${SLACK_WEBHOOK}

COPY . /opt/prefect/flows

WORKDIR /opt/prefect/flows

# Prefect 에이전트 실행
CMD ["python", "./flow.py"]