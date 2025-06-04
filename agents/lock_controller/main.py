import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.base_agent import BaseAgent

class LockController(BaseAgent):
    def run(self):
        print(f"[{self.name}] Running LockController logic...")
        self.publish("LockController processed task")

if __name__ == "__main__":
    config = {"name": "LockController", "topic": "lockcontroller"}
    agent = LockController(config)
    agent.run()
