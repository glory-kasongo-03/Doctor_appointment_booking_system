import copy

class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def clone(self):
        return copy.deepcopy(self)
