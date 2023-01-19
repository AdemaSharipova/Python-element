import re
import sys

from cmdProject.cmd.exceptions import UserInputException
from cmdProject.cmd.repositories import CMDRepositories
from cmdProject.cmd.services import CMDServices
from cmdProject.cmd.handlers import CMDHandlers


def init():
    cmd_repositories = CMDRepositories()
    cmd_services = CMDServices(repositories=cmd_repositories)
    cmd_handlers = CMDHandlers(services=cmd_services)

    while True:
        print(cmd_handlers.get_directory())
        command = input()

        if re.match(r'^cd \w+', command) or re.match(r'^(cd \.\.)$', command):
            cmd_handlers.change_directory(command)
        elif command == 'ls':
            cmd_handlers.list_directories(command)
        elif re.match(r'ls \w+', command):
            cmd_handlers.list_directories(command)
        elif re.match(r'mkdir \w+', command):
            cmd_handlers.create_directory(command)
        elif re.match(r'touch \w+', command):
            cmd_handlers.create_file_with_touch(command)
        elif re.match(r'echo \w+ > \w+', command):
            cmd_handlers.create_file_with_echo(command)
        elif re.match(r'mv\s+(\w+(\.\w+)?|\w+)\s+(\w+(\.\w+)?|\w+)', command):
            cmd_handlers.rename_file(command)
        elif re.match(r'rm \w+', command):
            cmd_handlers.delete_file(command)
        elif re.match(r'rm -r \w+', command):
            cmd_handlers.delete_dir(command)
        elif re.match(r'open \w+', command):
            cmd_handlers.open_file(command)
        elif command == "q":
            sys.exit()
        else:
            try:
                raise UserInputException
            except UserInputException as e:
                print(repr(e))


if __name__ == "__main__":
    init()