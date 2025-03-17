from dataclasses import dataclass
from pathlib import Path


@dataclass(kw_only=True)
class Client:
    rac_cli_path: Path | str
