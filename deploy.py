import os

from prefect.deployments import DeploymentImage
from prefect.client.schemas.schedules import CronSchedule

from flow import send_slack_flow

if __name__ == "__main__":
    send_slack_flow.deploy(
        name="test-prefect-slack-deployment",
        work_pool_name="docker-agent-pool",
        work_queue_name="docker-agent",
        image=DeploymentImage(
            name="test-prefect-slack",
            tag="1.0.1",
            dockerfile="Dockerfile",
            platform="linux/arm64",
            buildargs={"SLACK_WEBHOOK": os.getenv("SLACK_WEBHOOK")},
        ),
        schedule=(CronSchedule(cron="0 8 * * *", timezone="Asia/Seoul")),
        build=True,
    )