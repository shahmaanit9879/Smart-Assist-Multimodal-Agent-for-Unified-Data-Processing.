from src.logger import log_event

class A2AProtocol:
    def send(self, sender, receiver, message):
        log_event(f"{sender} → {receiver}: {message}")
        return {
            "from": sender,
            "to": receiver,
            "message": message,
            "status": "delivered"
        }
