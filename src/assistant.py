from agents import TextAgent, ImageAgent, MultiModalAgent

class SmartAssistAI:
    def safe_execute(self, func, *args):
    try:
        return func(*args)
    except Exception as e:
        return {"error": str(e)}
    def __init__(self):
        self.text_agent = TextAgent()
        self.image_agent = ImageAgent()
        self.multi_agent = MultiModalAgent()

    def text(self, text):
        return self.text_agent.process(text)

    def image(self, path):
        return self.image_agent.process(path)

    def multimodal(self, text, path):
        return self.multi_agent.process(text, path)
