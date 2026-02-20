from .client import AsyncClient
from ..cmd.command import Command
from ..errors import RACNotFoundError

import asyncio

class AsyncSession:
    def __init__(self, async_client: AsyncClient, host: str = "localhost", port: int = 1545, debug: bool = False) -> None:
        self.client = async_client
        self.host = host
        self.port = port
        self._debug = debug
    
    async def async_exec(self, command: Command):
        args: list[str] = [
            f"{self.host}:{self.port}",
        ] + command.args
        if self._debug:
            print("[DEBUG]", args)
        try:
            process = await asyncio.create_subprocess_exec("echo", "1")
            stdout, stderr = await process.communicate()
            if stdout:
                print(f'[stdout]\n{stdout.decode()}')
            if stderr:
                print(f'[stderr]\n{stderr.decode()}')
        except FileNotFoundError:
            raise RACNotFoundError

    async def async_call(self, command: Command):
        await self.async_exec(command)