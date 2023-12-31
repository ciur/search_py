from pathlib import PosixPath
from search_py.filedb import Record, write, read


def test_write_read_one_record(tmp_path: PosixPath):
    """Test case scenario with one record only

    Posting list in the record has only one item:

        a => [1]
    """
    path = tmp_path / "sub"
    path.mkdir()
    index_db = path / "index.db"
    records = [
        Record(term="a", postings=[1]),
    ]

    with open(index_db, 'wb') as f:
        write(f, records)

    with open(index_db, 'rb') as f:
        actual_records = read(f)

    assert actual_records == records


def test_write_read_one_record_with_two_postings(tmp_path: PosixPath):
    """Test case scenario with one record only

    Posting list in the record has two items:

        a => [1, 2]
    """
    path = tmp_path / "sub"
    path.mkdir()
    index_db = path / "index.db"
    records = [
        Record(term="term1", postings=[1, 2]),
    ]

    with open(index_db, 'wb') as f:
        write(f, records)

    with open(index_db, 'rb') as f:
        actual_records = read(f)

    assert actual_records == records


def test_write_read_two_records_with_two_postings_each(tmp_path: PosixPath):
    """Test case scenario with three records:

        term1 => [1, 2]
        term2 => [8, 3, 5]
        term3 => [9]
    """
    path = tmp_path / "sub"
    path.mkdir()
    index_db = path / "index.db"

    records = [
        Record(term="term1", postings=[1, 2]),
        Record(term="term2", postings=[8, 3, 5]),
        Record(term="term3", postings=[9]),
    ]

    with open(index_db, 'wb') as f:
        write(f, records)

    with open(index_db, 'rb') as f:
        actual_records = read(f)

    assert actual_records == records
