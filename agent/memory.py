class Memory:
    def __init__(self):
        self.data = []

    def store(self, content):
        self.data.append(content)

    def recall_all(self):
        return self.data


