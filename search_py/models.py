from tokenize import TokenInfo
from pathlib import Path
from typing import NamedTuple


class Document(NamedTuple):
    doc_id: int
    token: TokenInfo
    path: Path


class Record(NamedTuple):
    term: str
    postings: list[int]


class RecordHeader(NamedTuple):
    term_size: int
    posting_size: int
