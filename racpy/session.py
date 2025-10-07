from typing import TypeVar, Callable
from subprocess import run

from .client import Client
from .cmd.command import Command
from . import errors

T = TypeVar("T")


class Session:
    def __init__(self, client: Client, host: str = "localhost", port: int = 1545):
        self.client = client
        self.host = host
        self.port = port

    def exec(self, command: Command, handler: Callable[[str], T] = None) -> T | None:
        args = [
            self.client.rac_path,
            f"{self.host}:{self.port}",
        ] + command.args
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
