FROM prefecthq/prefect:2.18.3-python3.10

ARG SLACK_WEBHOOK

ENV SLACK_WEBHOOK=${SLACK_WEBHOOK}

# 작업 디렉토리 설정
COPY requirements.txt .

# 필요한 파이썬 패키지 설치
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /opt/prefect/flows

WORKDIR /opt/prefect/flows

# Prefect 에이전트 실행
CMD ["python", "./flow.py"]