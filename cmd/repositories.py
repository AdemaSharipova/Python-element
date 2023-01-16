import os

from exceptions import UserInputException


class CMDRepositories:

    def __init__(self):
        self.start_directory = '/'
        os.chdir(self.start_directory)

    def run(self) -> None:
        print(self.start_directory)
        while True:
            command = input()
            if command.startswith('cd'):
                try:
                    current_cd_command, new_directory = command.split()
                    print(self.change_directory(current_cd_command=current_cd_command, new_directory=new_directory))
                except:
                    print('It is not possible. Reformat your request')
            elif command.startswith('ls'):
                ls = self.list_directories()
                for e in ls:
                    print(e)
            elif command.startswith('mkdir'):
                try:
                    current_cd_command, new_directory_or_file = command.split()
                    print(self.create_directory(current_cd_command, new_directory_or_file))
                except UserInputException as e:
                    print(e)

    """ ---------------------------------------------------------------------- """

    # change directory:
    # cd 'directory' - go to 'directory'
    # cd '..' - go back one directory
    def change_directory(self, current_cd_command: str, new_directory: str) -> str:
        try:
            os.chdir(new_directory)
            self.start_directory = os.getcwd()
        except FileNotFoundError:
            print(f'{current_cd_command}: no such file or directory: {new_directory}')
        except NotADirectoryError:
            print(f'{current_cd_command}: not a directory: {new_directory}')
        except PermissionError:
            print(f'zsh: permission denied: {new_directory}')
        except UserInputException as e:
            print(e)
        return self.start_directory

    """ ---------------------------------------------------------------------- """

    def list_directories(self) -> list:
        return os.listdir(self.start_directory)

    """ ---------------------------------------------------------------------- """

    def create_directory(self, command: str, directory: str) -> str:
        try:
            os.mkdir(directory)
        except FileExistsError as e:
            print(f'{command}: {directory}: {e.strerror}')
        except PermissionError:
            print(f'zsh: permission denied: {directory}')
        except UserInputException as e:
            print(e)

        return self.start_directory

    def create_file(self) -> str:
        ...
    # cd Users/adema/Desktop


cmd = CMDRepositories()
cmd.run()
