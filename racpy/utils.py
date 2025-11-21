from typing import Type, TypeVar

T = TypeVar("T")


def get_array_chunks(arr: list[tuple], n: int) -> list[list]:
    return [arr[i : i + n] for i in range(0, len(arr), n)]


def get_dict_entry_count(output_lines: list[str]) -> int:
    idx = 0
    for line in output_lines:
        if line == "":
            return idx
        idx += 1


def b2yn(b: bool) -> str:
    match b:
        case True:
            return "yes"
        case False:
            return "no"
        case None:
            return None


def b2of(b: bool) -> str:
    match b:
        case True:
            return "on"
        case False:
            return "off"
        case None:
            return None


def b2da(b: bool) -> str:
    match b:
        case True:
            return "allow"
        case False:
            return "deny"
        case None:
            return None


def b2ana(b: bool) -> str:
    match b:
        case True:
            return "analyze"
        case False:
            return "not-analyze"
        case None:
            return None


def any2b(an: str) -> bool | str:
    match an:
        case "yes":
            return True
        case "no":
            return False
        case "on":
            return True
        case "off":
            return False
        case "allow":
            return True
        case "deny":
            return False
        case "analyze":
            return True
        case "not-analyze":
            return False
        case _:
            return an


def to_dc(entry: dict, dc: Type[T]) -> T:
    for key in entry:
        entry[key] = any2b(entry[key])
    return dc(**entry)


def list_to_dc(entry_list: list[dict], dc: Type[T]) -> list[T]:
    return [dc(**entry) for entry in entry_list]
