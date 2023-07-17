from typing import Tuple, Any


from search_py.tknizer import tokenizer_iter
from search_py.models import Document, Record
from search_py import filedb


def prepare_index(folder: str) -> Tuple[
    dict[Any, list[Document]],
    list[Document]
]:
    all_docs = []
    result = {}

    for doc in tokenizer_iter(folder):
        all_docs.append(doc)

        if not result.get(doc.token.string, None):
            result[doc.token.string] = [doc]
        else:
            # increases length of value
            result[doc.token.string].append(doc)

    return dict(sorted(result.items())), all_docs


def write_index_txt(file_name: str, docs: list[Document]) -> None:
    with open(file_name, 'w') as f:
        for doc in docs:
            f.write(f'{doc.doc_id},{doc.path}:{doc.token.start[0]}\n')


def write_index_db(file_name: str, sorted_dict: dict[Any, list[Document]]):
    records = [
        Record(term=key, postings=[doc.doc_id for doc in value])
        for key, value in sorted_dict.items()
    ]
    with open(file_name, 'wb') as f:
        filedb.write(f, records)


def get_postings(q: str) -> list[int] | None:
    with open('index.db', 'rb') as f:
        records = filedb.read(f)

    for record in records:
        if record.term.lower() == q.lower():
            return record.postings


def find(q: str) -> list[str] | None:
    postings = get_postings(q)

    if not postings:
        return []

    results = []

    with open('index.txt', 'r') as f:
        for number, line in enumerate(f):
            if number in postings:
                _, full_path = line.strip().split(',')
                results.append(full_path)

    return results
