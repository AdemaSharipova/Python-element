import re

from interfaces import CMDServicesInterface


class CMDHandlers:
    services: CMDServicesInterface

    def __init__(self, services) -> None:
        self.services = services

    def get_directory(self):
        return self.services.get_directory()

    def change_directory(self, command: str) -> None:
        command.strip()
        try:
            current_cd_command, new_directory = command.split()
            self.services.change_directory(current_cd_command=current_cd_command, new_directory=new_directory)
        except ValueError:
            print(f'cd: string not in pwd')

    def list_directories(self, command: str) -> list or str:
        command.strip()
        if re.match('ls \w+', command):
            current_command, directory = command.split()
            kwargs = {"command": current_command, "directory": directory}
            self.services.list_directories(full_command=command, **kwargs)
        elif command == "ls":
            self.services.list_directories(full_command=command)

    def create_directory(self, command: str) -> None:
        command.strip()
        current_command, new_directory = command.split(maxsplit=1)
        directories = new_directory.split()
        self.services.create_directory(current_command=current_command, directories=directories)

    def create_file_with_touch(self, command: str) -> None:
        command.strip()
        current_command, new_file = command.split(maxsplit=1)
        new_files = new_file.split()
        self.services.create_file(current_command=current_command, file=new_files)

    def create_file_with_echo(self, command: str) -> None:
        command.strip()
        current_command, text, file = command.split(maxsplit=2)
        file_to = file.split('> ')[1]
        self.services.create_file(current_command=current_command, file=file_to, text=text)

    def rename_file(self, command: str) -> None:
        command.strip()
        current_command, file1, file2 = command.split(maxsplit=3)
        self.services.rename_file(current_command=current_command, file1=file1, file2=file2)

    def delete_file(self, command: str) -> None:
        command.strip()
        current_command, new_file = command.split(maxsplit=1)
        files = new_file.split()
        self.services.delete_file_or_directory(current_command=current_command, command=command, files=files)

    def delete_dir(self, command: str) -> None:
        command.strip()
        current_command, new_file = command.split(maxsplit=1)
        files = str(new_file.split('-r ')[1])
        self.services.delete_file_or_directory(current_command=current_command, command=command, files=files)

    def open_file(self, command: str) -> None:
        command.strip()
        current_command, file = command.split(maxsplit=1)
        files = file.split()
        self.services.open_file(current_command=current_command, files=files)
