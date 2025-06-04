import redis
import threading
import json

class MessageBus:
    def __init__(self, redis_url="redis://localhost:6379/0"):
        self.redis = redis.Redis.from_url(redis_url)

    def publish(self, topic, message):
        payload = json.dumps(message)
        self.redis.publish(topic, payload)

    def subscribe(self, topic, callback):
        def listen():
            pubsub = self.redis.pubsub()
            pubsub.subscribe(topic)
            print(f"[MessageBus] Subscribed to {topic}")
            for msg in pubsub.listen():
                if msg["type"] == "message":
                    try:
                        data = json.loads(msg["data"])
                        callback(data)
                    except Exception as e:
                        print(f"[MessageBus] Error in callback: {e}")

        thread = threading.Thread(target=listen, daemon=True)
        thread.start()
