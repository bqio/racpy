from .utils import get_array_chunks, get_dict_entry_count

import re

LIST_DICT_REGEX = r"(.*?)\s+:\s?(.*)"


def to_str(instr: str) -> str:
    return instr.strip()


def to_dict(instr: str) -> dict[str, str]:
    matches = re.findall(LIST_DICT_REGEX, instr)
    _dict = {}
    for prop in matches:
        if prop[1].isdecimal():
            _dict[prop[0].replace("-", "_")] = int(prop[1])
        else:
            _dict[prop[0].replace("-", "_")] = prop[1].replace('"', "")
    return _dict


def to_list(instr: str) -> list[dict[str, str]]:
    entry_count = get_dict_entry_count(instr.split("\n"))
    matches = re.findall(LIST_DICT_REGEX, instr)
    chunks = get_array_chunks(matches, entry_count)
    _list = []
    for chunk in chunks:
        _dict = {}
        for prop in chunk:
            if prop[1].isdecimal():
                _dict[prop[0].replace("-", "_")] = int(prop[1])
            else:
                _dict[prop[0].replace("-", "_")] = prop[1].replace('"', "")
        _list.append(_dict)
    return _list
