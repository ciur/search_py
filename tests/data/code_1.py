from tokenize import TokenInfo
from pathlib import Path
from typing import NamedTuple


class Document(NamedTuple):
    doc_id: int
    token: TokenInfo
    path: Path
