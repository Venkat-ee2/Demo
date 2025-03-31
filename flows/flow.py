from prefect import task, flow

@task
def say_hello():
    print("hello world!")

@flow
def flow():
    say_hello()

if __name__ == "__main__":
    flow()
