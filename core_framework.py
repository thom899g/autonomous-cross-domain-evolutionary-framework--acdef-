import zmq
from typing import Dict, Any

class MessageBroker:
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        self.subscriptions: Dict[str, str] = {}

    def subscribe(self, module_id: str, topic: str) -> None:
        """Subscribe a module to receive messages on a specific topic."""
        self.socket.subscribe(topic)
        self.subscriptions[module_id] = topic

    def publish_message(self, topic: str, message: Dict[str, Any]) -> None:
        """Publish a message to a specific topic."""
        try:
            self.socket.send_json({"topic": topic, "message": message})
            logging.info(f"Published message on topic: {topic}")
        except zmq.ZMQError as e:
            logging.error(f"Failed to publish message: {e}")

    def close(self) -> None:
        """Close the message broker."""
        self.socket.close()
        self.context.term()