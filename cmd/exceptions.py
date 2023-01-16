class UserInputException(Exception):
    def __init__(self):
        self.message = 'It is not possible. Reformat your request'

    def __repr__(self):
        return self.message


def common_exceptions(command, current_cd_command,new_directory):
    try:
        command
    except FileNotFoundError:
        print(f'{current_cd_command}: no such file or directory: {new_directory}')
    except NotADirectoryError:
        print(f'{current_cd_command}: not a directory: {new_directory}')
    except PermissionError:
        print(f'zsh: permission denied: {new_directory}')
    except UserInputException as e:
        print(e)

