import struct
from typing import NamedTuple


header = struct.Struct("<ii")


def text(field: bytes) -> str:
    return field.decode('utf-8')


class RecordHeader(NamedTuple):
    term_size: int
    posting_size: int


class Record(NamedTuple):
    term: str
    postings: list[int]


def write(f, records: list[Record]):
    f.write(struct.pack('<i', len(records)))
    for record in records:
        term_bytes = record.term.encode('utf-8')
        term_len = len(term_bytes)
        f.write(
            struct.pack('<ii', term_len, len(record.postings))
        )
        f.write(term_bytes)

        for item in record.postings:
            f.write(struct.pack('<i', item))


def read(f) -> list[Record]:
    result = []
    records_count = struct.unpack('<i', f.read(4))[0]

    for _ in range(0, records_count):
        header = RecordHeader._make(
            struct.unpack('<ii', f.read(8))
        )
        term = text(f.read(header.term_size))
        postings = []
        for _ in range(0, header.posting_size):
            postings.append(
                struct.unpack('<i', f.read(4))[0]
            )

        rec = Record(term=term, postings=postings)

        result.append(rec)

    return result
