from typing import Protocol


class CMDRepositoriesInterface(Protocol):
    start_directory: str

    def __init__(self) -> None:
        raise NotImplementedError

    def get_directory(self):
        raise NotImplementedError

    def change_directory(self, current_cd_command: str, new_directory: str) -> None:
        raise NotImplementedError

    def list_directories(self, full_command: str, **kwargs) -> None or str:
        raise NotImplementedError

    def create_directory(self, current_command: str, directories: list) -> None:
        raise NotImplementedError

    def create_file(self, current_command: str, file: list or str, **kwargs) -> None:
        raise NotImplementedError

    def rename_file(self, current_command: str, file1: str, file2: str) -> None:
        raise NotImplementedError

    def delete_file_or_directory(self, current_command: str, command: str, files: str or list) -> None:
        raise NotImplementedError

    def open_file(self, current_command: str, files: str or list) -> None:
        raise NotImplementedError


class CMDServicesInterface(Protocol):
    start_directory: str

    def __init__(self) -> None:
        raise NotImplementedError

    def get_directory(self):
        raise NotImplementedError

    def change_directory(self, current_cd_command: str, new_directory: str) -> None:
        raise NotImplementedError

    def list_directories(self, full_command: str, **kwargs) -> None or str:
        raise NotImplementedError

    def create_directory(self, current_command: str, directories: list) -> None:
        raise NotImplementedError

    def create_file(self, current_command: str, file: list or str, **kwargs) -> None:
        raise NotImplementedError

    def rename_file(self, current_command: str, file1: str, file2: str) -> None:
        raise NotImplementedError

    def delete_file_or_directory(self, current_command: str, command: str, files: str or list) -> None:
        raise NotImplementedError

    def open_file(self, current_command: str, files: str or list) -> None:
        raise NotImplementedError







