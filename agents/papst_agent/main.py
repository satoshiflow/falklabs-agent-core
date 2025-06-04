import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.base_agent import BaseAgent
from shared.message_bus import MessageBus
import time

class PapstAgent(BaseAgent):
    def run(self):
        bus = MessageBus()
        print(f"[{self.name}] Sende Gesundheitsfrage an Bischöfe...")
        bus.publish("bischof-frage", {"from": self.name, "msg": "Seid ihr alle da und gesund?"})

        def callback(msg):
            print(f"[{self.name}] Antwort vom Kardinal: {msg['msg']}")

        bus.subscribe("papst-status", callback)
        while True:
            time.sleep(1)

if __name__ == "__main__":
    config = {"name": "PapstAgent", "topic": "papst-status"}
    agent = PapstAgent(config)
    agent.run()
