from cmdProject.cmd.interfaces import CMDRepositoriesInterface


class CMDServices():
    start_directory: str
    repositories: CMDRepositoriesInterface

    def __init__(self, repositories) -> None:
        self.repositories = repositories
        self.start_directory = self.repositories.start_directory

    def get_directory(self):
        return self.repositories.get_directory()

    def change_directory(self, current_cd_command: str, new_directory: str) -> None:
        self.repositories.change_directory(current_cd_command=current_cd_command, new_directory=new_directory)

    def list_directories(self, full_command: str, **kwargs) -> None or str:
        self.repositories.list_directories(full_command=full_command, **kwargs)

    def create_directory(self, current_command: str, directories: list) -> None:
        self.repositories.create_directory(current_command=current_command, directories=directories)

    def create_file(self, current_command: str, file: list or str, **kwargs) -> None:
        self.repositories.create_file(current_command=current_command, file=file, **kwargs)

    def rename_file(self, current_command: str, file1: str, file2: str) -> None:
        self.repositories.rename_file(current_command=current_command, file1=file1, file2=file2)

    def delete_file_or_directory(self, current_command: str, command: str, files: str or list) -> None:
        self.repositories.delete_file_or_directory(current_command=current_command, command=command, files=files)

    def open_file(self, current_command: str, files: str or list) -> None:
        self.repositories.open_file(current_command=current_command, files=files)
