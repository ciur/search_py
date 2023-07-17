import typer

from search_py.tknizer import tokenizer_iter
from search_py.index import (
    prepare_index,
    write_index_txt,
    write_index_db,
    find
)

app = typer.Typer()


@app.command()
def index(folder: str):
    sorted_dict, all_docs = prepare_index(folder)
    docs = sorted(all_docs, key=lambda item: item.doc_id)
    write_index_txt('index.txt', docs)
    write_index_db('index.db', sorted_dict)


@app.command()
def stats(folder: str, top_count: int = 20):
    """Display stats of most frequent tokens"""
    results = {}
    # count frequency of each token
    for doc in tokenizer_iter(folder):
        if not results.get(doc.token.string, None):
            results[doc.token.string] = [doc]
        else:
            # increases length of value
            results[doc.token.string].append(doc)

    # sort tokens by their frequency (i.e. length of value)
    sorted_results = sorted(
        results,
        key=lambda k: len(results[k]), reverse=True
    )

    for top in range(top_count):
        token = sorted_results[top]
        print(f'{token},{len(results[token])}')


@app.command()
def search(q: str):
    results = find(q)

    if not results:
        print("Not found")

    for result in results:
        print(result)


if __name__ == "__main__":
    app()
