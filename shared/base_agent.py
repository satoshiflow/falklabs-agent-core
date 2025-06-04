import redis
import json
import uuid

class BaseAgent:
    def __init__(self, config, redis_url="redis://localhost:6379/0"):
        self.name = config.get("name", "UnnamedAgent")
        self.topic = config.get("topic", "default")
        self.id = str(uuid.uuid4())
        self.redis = redis.Redis.from_url(redis_url)
        print(f"[{self.name}] Initialized with ID {self.id}")

    def publish(self, message):
        payload = json.dumps({"agent": self.name, "message": message})
        self.redis.publish(self.topic, payload)
        print(f"[{self.name}] Published: {message}")
