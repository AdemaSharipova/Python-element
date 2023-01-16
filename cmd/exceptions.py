class UserInputException(Exception):
    def __init__(self):
        self.message = 'It is not possible. Reformat your request'

    def __repr__(self):
        return self.message



