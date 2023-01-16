from typing import Protocol


class CMDRepositoriesInterfaces(Protocol):

    def __init__(self):
        raise NotImplementedError

    def change_directory(self, current_cd_command: str, new_directory: str) -> str:
        raise NotImplementedError

    def list_directories(self) -> str:
        raise NotImplementedError

    def create_directory(self) -> str:
        raise NotImplementedError

    def create_file(self) -> str:
        raise NotImplementedError









