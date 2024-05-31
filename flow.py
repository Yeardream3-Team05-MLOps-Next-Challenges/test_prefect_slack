from prefect import flow
from prefect.deployments import DeploymentImage

@flow(log_prints=True)
def hello():
  print("Hello!")

if __name__ == "__main__":
    hello.deploy(
        name="test-prefect-docker-deployment",
        work_pool_name="docker-agent-pool",
        work_queue_name="docker-agent",
        #image="test-prefect-docker:0.1",
        image=DeploymentImage(
            name="test-prefect-docker",
            tag="0.3",
            buildargs={"PYTHON_VERSION": "3.10"},
            platform="linux/arm64"
        ),
        cron="0 * * * *",
    )