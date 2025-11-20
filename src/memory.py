class AgentMemory:
    def __init__(self):
        self.logs = []

    def remember(self, message):
        self.logs.append(message)

    def get_memory(self):
        return self.logs[-5:]  # last 5 messages
