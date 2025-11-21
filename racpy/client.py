from pathlib import Path


class Client:
    def __init__(self, rac_path: Path | str):
        """
        Класс представляет клиент для подключения к консольной утилите
        1С Remote Administrative Client.

        Args:
            rac_path (Path | str): Абсолютный путь до консольной утилиты.
        """
        self.rac_path = rac_path
