from .agents import TextAgent, ImageAgent
from .logger import log_event

class CoordinatorAgent:
    def __init__(self):
        self.text_agent = TextAgent()
        self.image_agent = ImageAgent()

    def route(self, data):
        if isinstance(data, str):
            log_event("Coordinator", "Routing to TextAgent")
            return self.text_agent.process(data)
        else:
            log_event("Coordinator", "Routing to ImageAgent")
            return self.image_agent.process(data)
