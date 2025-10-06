def get_array_chunks(arr: list[tuple], n: int) -> list[list]:
    return [arr[i : i + n] for i in range(0, len(arr), n)]


def get_dict_entry_count(output_lines: list[str]) -> int:
    idx = 0
    for line in output_lines:
        if line == "":
            return idx
        idx += 1


def b2yn(b: bool) -> str:
    return "yes" if b else "no"


def b2of(b: bool) -> str:
    return "on" if b else "off"


def b2da(b: bool) -> str:
    return "allow" if b else "deny"


def b2ana(b: bool) -> str:
    return "analyze" if b else "not-analyze"
