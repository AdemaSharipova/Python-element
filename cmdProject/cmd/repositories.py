import os
import subprocess
import re
import shutil

from cmdProject.cmd.exceptions import common_exceptions


class CMDRepositories():
    start_directory: str

    def __init__(self) -> None:
        self.start_directory = '/'
        os.chdir(self.start_directory)

    """ ------------------------GET-DIRECTORY--------------------------------------------- """

    def get_directory(self):
        return self.start_directory

    """ ------------------------CHANGE-DIRECTORY------------------------------------------- """
    def change_directory(self, current_cd_command: str, new_directory: str) -> None:
        try:
            os.chdir(new_directory)
            self.start_directory = os.getcwd()
        except IOError as e:
            print(common_exceptions(e=e, current_command=current_cd_command, new_directory=new_directory))

    """ --------------------LIST-DIRECTORIES------------------------------------------------ """

    def list_directories(self, full_command: str, **kwargs) -> None or str:
        li = list
        try:
            if full_command == 'ls':
                li = list(it for it in os.listdir(self.start_directory) if it.startswith('.') == False)

            elif re.match('ls \w+', full_command):
                li = list(it for it in os.listdir(f'{self.start_directory}/{kwargs.get("directory")}') if it.startswith('.') == False)

        except OSError as e:
            if e.errno == 1:
                print(common_exceptions(e=e, current_command=full_command))
                return ''
            print(common_exceptions(e=e, current_command=kwargs.get('command'), new_directory=kwargs.get('directory')))
            return ''

        for i in sorted(li):
            print(i)

    """ --------------------CREATE-DIRECTORY------------------------------------------------- """

    def create_directory(self, current_command: str, directories: list) -> None:
        for i in range(0, len(directories)):
            try:
                os.mkdir(directories[i])
            except Exception as e:
                print(common_exceptions(e, current_command, directories[i]))

    """ ---------------------CREATE-FILE------------------------------------------------ """

    def create_file(self, current_command: str, file: list or str, **kwargs) -> None:
        if type(file) == str:
            file = [file]
        for i in range(0, len(file)):
            try:
                with open(file[i], mode='w') as f:
                    os.utime(f'{self.start_directory}/{file[i]}')
                    if current_command == 'echo':
                        f.write(kwargs.get('text'))
            except OSError as e:
                if e.errno != 2 and type(file) != str:
                    print(common_exceptions(e, current_command, file[i]))

    """ ----------------------RENAME-FILE----------------------------------------------- """
    def rename_file(self, current_command: str, file1: str, file2: str) -> None:
        try:
            os.rename(file1, file2)
        except OSError as e:
            if e.errno == 2:
                e.errno = 'MyErrorID1'
            print(common_exceptions(e, current_command, file1))

    """ ----------------------DELETE-FILE-OR-DIRECTORY-------------------------------------- """

    def delete_file_or_directory(self, current_command: str, command: str, files: str or list) -> None:
        if type(files) == str:
            files = [files]
        for i in range(0, len(files)):
            try:
                if re.match(r'rm -r \w+', command):
                    shutil.rmtree(f'{self.start_directory}/{files[i]}')
                    if os.path.isfile(f'{self.start_directory}/{files[i]}'):
                        try:
                            raise NotADirectoryError
                        except NotADirectoryError as e:
                            print(common_exceptions(e, current_command, files[i]))
                elif re.match(r'rm \w+', command):
                    if os.path.isdir(f'{self.start_directory}/{files[i]}'):
                        try:
                            raise IsADirectoryError
                        except IsADirectoryError as e:
                            e.errno = 21
                            e.strerror = 'is a directory'
                            print(common_exceptions(e, current_command=current_command, new_directory=files[i]))
                    os.remove(f'{self.start_directory}/{files[i]}')

            except PermissionError:
                assert True
            except OSError as e:
                print(common_exceptions(e, current_command, files[i]))

    """ ---------------------------OPEN-FILE------------------------------------------ """

    def open_file(self, current_command: str, files: str or list) -> None:
        for i in range(0, len(files)):
            try:
                file_path = f'{self.start_directory}/{files[i]}'
                subprocess.Popen(["open", file_path])
            except OSError as e:
                print(common_exceptions(e, current_command, files[i]))




