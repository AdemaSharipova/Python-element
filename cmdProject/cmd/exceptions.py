class UserInputException(Exception):
    def __init__(self):
        self.message = 'It is not possible. Reformat your request'

    def __repr__(self):
        return self.message


def common_exceptions(e, current_command, new_directory=None):
    """
    20 - Not a directory | NotADirectoryError
    2 - No such file or directory | FileNotFoundError
    1 - Permission denied | PermissionError
    17 - File exists | FileExistsError
    """

    if e.errno == 20 or e.errno == 2:
        return f'{current_command}: {e.strerror}: {new_directory}'
    elif e.errno == 17:
        return f'{current_command}: {new_directory}: {e.strerror}'
    elif e.errno == 1:
        return f'zsh: {e.strerror}: {current_command}'
    elif e.errno == 'MyErrorID1':
        return f'{current_command}: rename {e.filename} to {e.filename2}: {e.strerror}'
    elif e.errno == 13:
        return f'{current_command}: {e.strerror}: {new_directory}'
    elif e.errno == 21:
        return f'{current_command}: {new_directory}: {e.strerror}'
    else:
        return f'{e.errno}: {e.strerror}'





