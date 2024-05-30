from prefect import flow

@flow(log_prints=True)
def hello():
  print("Hello!")

if __name__ == "__main__":
    hello.deploy(
        name="test-prefect-docker-deployment",
        work_pool_name="docker-agent-pool",
        work_queue_name="docker-agent",
        image="test-prefect-docker:0.1",
        cron="0 * * * *",
    )