class Memory:
    def __init__(self):
        self.data = []
        self.source_metadata = []

    def store(self, content, metadata):
        self.data.append(content)
        self.source_metadata.append({
            "title": metadata.get("title", "Unknown"),
            "url": metadata.get("url", ""),
            "author": metadata.get("author", "Unknown"),
            "date": metadata.get("date", "")
        })

    def recall_all(self):
        return list(zip(self.data, self.source_metadata))
