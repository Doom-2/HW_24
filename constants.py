import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

CORRECT_QUERY_VALUES = [
    'filter',
    'map',
    'unique',
    'sort',
    'limit'
]

CORRECT_QUERY_KEYS = [
    'cmd1',
    'cmd2',
    'value1',
    'value2',
    'file_name'
]
