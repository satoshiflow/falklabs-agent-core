import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.base_agent import BaseAgent
from shared.message_bus import MessageBus
import time
import random

class BischofAgent(BaseAgent):
    def run(self):
        bus = MessageBus()

        def callback(msg):
            print(f"[{self.name}] Frage empfangen: {msg['msg']}")
            status = "OK" if random.random() > 0.3 else "FEHLER"
            time.sleep(random.randint(1, 3))
            bus.publish("kardinal-status", {"from": self.name, "msg": status})

        bus.subscribe("bischof-frage", callback)
        while True:
            time.sleep(1)

if __name__ == "__main__":
    config = {"name": "BischofAgent", "topic": "bischof-frage"}
    agent = BischofAgent(config)
    agent.run()
