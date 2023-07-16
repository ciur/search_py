import typer
from search_py.tknizer import tokenizer_iter

app = typer.Typer()


@app.command()
def index(folder: str):
    for path, token in tokenizer_iter(folder):
        print(path, token)


@app.command()
def main(q: str):
    print(f"Searching for... {q}")


if __name__ == "__main__":
    app()
