import PIL
import typer

app = typer.Typer()

@app.command()
def hello(name: str) -> int:
    print(f"Hello {name}")
    return 0


@app.command()
def create(fps: int = None) -> int:
    print(f"fps {fps}")
    return 0

def main():
    return app()
