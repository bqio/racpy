from typing import TypeVar, Callable
from subprocess import run

from .client import Client
from .cmd.command import Command
from . import errors

T = TypeVar("T")


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
        """
        self.client = client
        self.host = host
        self.port = port
        self._debug = debug

    def exec(self, command: Command, handler: Callable[[str], T] = None) -> T | None:
        args = [
            self.client.rac_path,
            f"{self.host}:{self.port}",
        ] + command.args
        if self._debug:
            print("[DEBUG] Command args:", args)
        try:
            process = run(
                args,
                capture_output=True,
                text=True,
                encoding="cp866",
            )
            if process.returncode != 0:
                raise errors.handler(process.stderr)
            if process.stdout == "":
                return None
            if handler:
                return handler(process.stdout)
            else:
                return None
        except FileNotFoundError:
            raise errors.RACNotFoundError
