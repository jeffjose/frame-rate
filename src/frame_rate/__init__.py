import typer

def main() -> int:
    typer.run(run)

def run(name: str) -> int:
    print("Hello {name}")
    return 0
