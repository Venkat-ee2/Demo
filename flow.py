from prefect import task, Flow

@task
def say_hello(name: str):
    print(f"Hello, {name}!")

with Flow("hello-flow") as flow:
    name = "World"  
    say_hello(name)


if __name__ == "__main__":
    flow.run()

