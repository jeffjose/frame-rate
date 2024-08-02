import typer

app = typer.Typer()

@app.command()
def hello(name: str) -> int:
    print(f"Hello {name}")
    return 0


@app.command()
def bye(name: str) -> int:
    print(f"Bye {name}")
    return 0

def main():
    return app()
