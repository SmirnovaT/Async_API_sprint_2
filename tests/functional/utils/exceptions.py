class EmptyIndexError(Exception):
    def __init__(self, index, message):
        self.index = index
        self.message = message

    def __str__(self):
        return f'{self.index}: {self.message}'
