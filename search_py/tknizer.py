import os
import tokenize
from pathlib import Path


def python_files_iter(folder: str):
    for root, dirs, files in os.walk(folder):
        filtered_files = [file for file in files if file.endswith('py')]
        if len(filtered_files):
            for file in files:
                yield Path(root) / Path(file)


def file_tokens_iter(file: Path):
    with open('stop.txt') as f:
        stop_words = [line.strip() for line in f.readlines()]

    with tokenize.open(file) as f:
        tokens = tokenize.generate_tokens(f.readline)
        for token in tokens:
            if token.string in stop_words:
                continue
            if len(token.string.strip()) == 0:
                continue
            yield token


def tokenizer_iter(folder: str):
    for path in python_files_iter(folder):
        for token in file_tokens_iter(path):
            yield path, token
