from time import sleep

def typer(input: str) -> None:
    for i in input:
        print(i, end='', flush=True)
        sleep(0.6)