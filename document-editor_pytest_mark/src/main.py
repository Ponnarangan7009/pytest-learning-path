class DocumentEditor:
    def __init__(self):
        self.content = ""
        self.history = []
        self.document_action = []

    def write(self, text):
        self.history.append(text)
        self.content += text
        self.document_action.append(f"added a new line: {text}")

    def clear(self):
        self.document_action.append(f"cleared the content: {self.content}")
        self.content = ""

    def is_empty(self):
        return self.content == ""

    def get_last_content(self):
        if len(self.history) == 0:
            raise ValueError("no document history available")
        return self.history[-1]
