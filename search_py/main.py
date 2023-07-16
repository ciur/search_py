import typer

app = typer.Typer()


@app.command()
def main(q: str):
    print(f"Searching for... {q}")


if __name__ == "__main__":
    app()
