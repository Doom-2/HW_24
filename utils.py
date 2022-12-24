import re
from re import Pattern
from typing import Any, Optional
from constants import CORRECT_QUERY_KEYS, CORRECT_QUERY_VALUES


def check_query(req_data: dict[str, Any]) -> None:

    if not set(req_data.keys()).issubset(CORRECT_QUERY_KEYS):
        raise KeyError('Query key(s) not allowed')

    if not {req_data.get('cmd1'), req_data.get('cmd2'), req_data.get('cmd3')}.issubset(CORRECT_QUERY_VALUES):
        raise ValueError('Query value(s) not allowed')


def get_data(file_name: str) -> list[str]:
    with open(file_name) as file:
        return list(map(lambda x: x.strip(), file))


def filter_query(param: str, data: list[str]) -> list[str]:
    return [line for line in filter(lambda x: param in x, data)]


def map_query(param: int, data: list[str]) -> list[str]:
    param = int(param)
    return list(map(lambda x: x.split(' ')[param], data))


def unique_query(data: list[str]) -> list[str]:
    return list(set(data))


def sort_query(param: Optional[str], data: list[str]) -> list[str]:
    if param == 'asc':
        reverse = False
    else:
        reverse = True
    return sorted(data, reverse=reverse)


def limit_query(param: int | str, data: list[str]) -> list[str]:
    param = int(param)
    return list(data)[:param]


def regex_query(param: str, data: list[str]) -> list[str]:
    regex: Pattern = re.compile(param)
    return list(filter(lambda x: re.findall(regex, x), data))


def get_data_by_query(req_data: dict[str, Any], data: list[str]) -> list[str]:
    """
    Applies an appropriate function to filter input data according request data.
    The query keys 'cmd1', 'cmd2' and 'cmd3' are used.
    :param req_data: request data from JSON or address line
    :param data: source file data
    :return: filtered file data
    """
    check_query(req_data)

    res: list[str] = data

    if 'cmd1' in req_data.keys():
        if req_data['cmd1'] == 'filter':
            res = filter_query(req_data['value1'], data)
        elif req_data['cmd1'] == 'map':
            res = map_query(req_data['value1'], data)
        elif req_data['cmd1'] == 'unique':
            res = unique_query(data)
        elif req_data['cmd1'] == 'sort':
            res = sort_query(req_data['value1'], data)
        elif req_data['cmd1'] == 'limit':
            res = limit_query(req_data['value1'], data)
        elif req_data['cmd1'] == 'regex':
            res = regex_query(req_data['value1'], data)
        else:
            res = data
    if 'cmd2' in req_data.keys():
        if req_data['cmd2'] == 'filter':
            res = filter_query(req_data['value2'], res)
        elif req_data['cmd2'] == 'map':
            res = map_query(req_data['value2'], res)
        elif req_data['cmd2'] == 'unique':
            res = unique_query(res)
        elif req_data['cmd2'] == 'sort':
            res = sort_query(req_data['value2'], res)
        elif req_data['cmd2'] == 'limit':
            res = limit_query(req_data['value2'], res)
        elif req_data['cmd2'] == 'regex':
            res = regex_query(req_data['value2'], res)
        else:
            res = data

    if 'cmd3' in req_data.keys():
        if req_data['cmd3'] == 'filter':
            res = filter_query(req_data['value3'], res)
        elif req_data['cmd3'] == 'map':
            res = map_query(req_data['value3'], res)
        elif req_data['cmd3'] == 'unique':
            res = unique_query(res)
        elif req_data['cmd3'] == 'sort':
            res = sort_query(req_data.get('value3'), res)
        elif req_data['cmd3'] == 'limit':
            res = limit_query(req_data['value3'], res)
        elif req_data['cmd3'] == 'regex':
            res = regex_query(req_data['value3'], res)
        else:
            res = data

    return res
