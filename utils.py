import json
import logging

from constants import DOWNLOAD_DIR


def read_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_data(data, file_name):
    DOWNLOAD_DIR.mkdir(exist_ok=True)
    file_path = DOWNLOAD_DIR / file_name
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def configure_logging():
    logging.basicConfig(
        datefmt='%d.%m.%Y %H:%M:%S',
        format='%(asctime)s - [%(levelname)s] - %(message)s',
        level=logging.INFO,
        )
