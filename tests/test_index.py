import os
from search_py.index import prepare_index

CURRENT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURRENT_DIR, "data")


def test_prepare_index():
    sorted_dict, all_docs = prepare_index(DATA_DIR)
    expected_result = {
        'Document': [7],
        'NamedTuple': [6, 8],
        'Path': [4, 14],
        'TokenInfo': [2, 12],
        'doc_id': [9],
        'int': [10],
        'path': [13],
        'pathlib': [3],
        'token': [11],
        'tokenize': [1],
        'typing': [5]
    }
    assert sorted_dict.keys() == expected_result.keys()

    for key, value in sorted_dict.items():
        assert key in expected_result.keys()
        assert expected_result[key] == list([k.doc_id for k in value])
