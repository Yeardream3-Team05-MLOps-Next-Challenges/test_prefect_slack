import os 
import requests
import json

from prefect import flow

@flow(log_prints=True)
def send_slack_flow():
    # 슬랙 웹훅 URL
    webhook_url = os.getenv("SLACK_WEBHOOK")

    # 전송할 메시지
    message = {
        'text': 'Good morning!'
    }

    # HTTP POST 요청을 통해 메시지 전송
    response = requests.post(
        webhook_url, 
        data=json.dumps(message), 
        headers={'Content-Type': 'application/json'}
    )

    # 응답 상태 코드 출력
    print('응답 상태 코드:', response.status_code)
    print('응답 내용:', response.text)


if __name__ == "__main__":
    send_slack_flow()