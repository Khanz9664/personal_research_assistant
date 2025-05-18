class Memory:
    """
    A simple class to store and recall pieces of information (memory).
    """

    def __init__(self):
        # Initialize an empty list to store memory content
        self.data = []

    def store(self, content):
        """
        Stores a new piece of content in memory.

        Parameters:
            content (any): The item to store in memory.
        """
        self.data.append(content)

    def recall_all(self):
        """
        Retrieves all stored content from memory.

        Returns:
            list: A list of all stored items.
        """
        return self.data

