from typing import TypeVar, Type
from subprocess import run

from .client import Client
from .cmd.command import Command
from . import errors
from .utils import get_array_chunks, dict_entry_count, any2b

import re

T = TypeVar("T")
LIST_DICT_REGEX = r"(.*?)\s+:\s?(.*)"


class RawOutput:
    def __init__(self, output: str) -> None:
        self.output = output

    def to_str(self) -> str:
        """
        Конвертировать сырой результат в `str`.
        """
        return self.output.strip()

    def to_dict(self) -> dict[str, str | int]:
        """
        Конвертировать сырой результат в `dict[str, str | int]`.
        """
        matches: list[tuple[str, str]] = re.findall(LIST_DICT_REGEX, self.output)
        _dict: dict[str, str | int] = {}
        for prop in matches:
            if prop[1].isdecimal():
                _dict[prop[0].replace("-", "_")] = int(prop[1])
            else:
                _dict[prop[0].replace("-", "_")] = prop[1].replace('"', "")
        for key in _dict:
            _dict[key] = any2b(_dict[key])
        return _dict

    def to_dataclass(self, dc: Type[T]) -> T:
        """
        Конвертировать сырой результат в `T`.
        """
        return dc(**self.to_dict())

    def to_list_of_dataclass(self, dc: Type[T]) -> list[T]:
        """
        Конвертировать сырой результат в `list[T]`.
        """
        return [dc(**entry) for entry in self.to_list()]

    def to_list(self) -> list[dict[str, str | int]]:
        """
        Конвертировать сырой результат в `list[dict[str, str | int]]`.
        """
        entry_count = dict_entry_count(self.output.split("\n"))
        matches: list[tuple[str, str]] = re.findall(LIST_DICT_REGEX, self.output)
        if matches == []:
            return []
        chunks = get_array_chunks(matches, entry_count)
        _list: list[dict[str, str | int]] = []
        for chunk in chunks:
            _dict: dict[str, str | int] = {}
            for prop in chunk:
                if prop[1].isdecimal():
                    _dict[prop[0].replace("-", "_")] = int(prop[1])
                else:
                    _dict[prop[0].replace("-", "_")] = prop[1].replace('"', "")
            for key in _dict:
                _dict[key] = any2b(_dict[key])
            _list.append(_dict)
        return _list


class Session:
    def __init__(
        self,
        client: Client,
        host: str = "localhost",
        port: int = 1545,
        debug: bool = False,
    ):
        """
        Класс представляет уникальную сессию для подключения к серверу администрирования.

        Args:
            client (Client): Клиент для подключения к консольной утилите
                1С Remote Administrative Client.
            host (str): Хост или IP адрес сервера администрирования.
            port (int): Порт сервера администрирования.
            debug (bool): Выводить дополнительную информацию в консоль для отладки.
        Returns:
            Session: Уникальная сессия.
        """
        self.client = client
        self.host = host
        self.port = port
        self._debug = debug

    def exec(self, command: Command) -> RawOutput:
        """
        Выполнить команду и вернуть сырой результат.

        Args:
            command (Command): Команда.

        Returns:
            RawOutput: Сырой результат.
        """
        args: list[str] = [
            str(self.client.rac_path),
            f"{self.host}:{self.port}",
        ] + command.args
        if self._debug:
            print("[DEBUG]", args)
        try:
            process = run(
                args,
                capture_output=True,
                text=True,
                encoding="cp866",
            )
            if process.returncode != 0:
                raise errors.handler(process.stderr)
            else:
                if self._debug:
                    print(process.stdout)
                return RawOutput(process.stdout)
        except FileNotFoundError:
            raise errors.RACNotFoundError

    def call(self, command: Command) -> None:
        """
        Выполнить команду без возврата результата.

        Args:
            command (Command): Команда.
        """
        self.exec(command)
