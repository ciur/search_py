import typer
from search_py.tknizer import tokenizer_iter

app = typer.Typer()


@app.command()
def index(folder: str):
    for path, token in tokenizer_iter(folder):
        print(path, token)


@app.command()
def stats(folder: str, top_count: int = 20):
    """Display stats of most frequent tokens"""
    results = {}
    # count frequency of each token
    for path, token in tokenizer_iter(folder):
        if not results.get(token.string, None):
            results[token.string] = [(path, token)]
        else:
            # increases length of value
            results[token.string].append((path, token))

    # sort tokens by their frequency (i.e. length of value)
    sorted_results = sorted(
        results,
        key=lambda k: len(results[k]), reverse=True
    )

    for top in range(top_count):
        token = sorted_results[top]
        print(f'{token},{len(results[token])}')


@app.command()
def main(q: str):
    print(f"Searching for... {q}")


if __name__ == "__main__":
    app()
