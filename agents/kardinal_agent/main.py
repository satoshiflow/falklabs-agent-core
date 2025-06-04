import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.base_agent import BaseAgent
from shared.message_bus import MessageBus
import time

class KardinalAgent(BaseAgent):
    def run(self):
        bus = MessageBus()
        self.responses = []

        def callback(msg):
            print(f"[{self.name}] Antwort von Bischof: {msg['from']} = {msg['msg']}")
            self.responses.append(msg)
            if len(self.responses) >= 2:
                all_ok = all(r["msg"] == "OK" for r in self.responses)
                result = "ALLE OK" if all_ok else "PROBLEM GELÖST"
                bus.publish("papst-status", {"from": self.name, "msg": result})
                self.responses.clear()

        bus.subscribe("kardinal-status", callback)
        while True:
            time.sleep(1)

if __name__ == "__main__":
    config = {"name": "KardinalAgent", "topic": "kardinal-status"}
    agent = KardinalAgent(config)
    agent.run()
