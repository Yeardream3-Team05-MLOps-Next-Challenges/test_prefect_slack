from prefect import flow
from prefect.deployments import DeploymentImage

from flows.flow import hello


if __name__ == "__main__":
    hello.deploy(
        name="test-prefect-docker-deployment",
        work_pool_name="docker-agent-pool",
        work_queue_name="docker-agent",
        image="test-prefect-docker:0.9",
        cron="0 * * * *",
        build=False
    )