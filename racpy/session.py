from dataclasses import dataclass
from typing import TypeVar, Callable
from subprocess import run

from .client import Client
from .cmd.command import Command
from . import errors

T = TypeVar("T")


@dataclass(kw_only=True)
class Session:
    host: str
    port: int
    client: Client

    def exec(self, command: Command, handler: Callable[[str], T] = None) -> str | None:
        args = [
            self.client.rac_cli_path,
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
