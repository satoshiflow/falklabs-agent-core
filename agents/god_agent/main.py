import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.base_agent import BaseAgent

class GodAgent(BaseAgent):
    def run(self):
        print(f"[{self.name}] I am the Creator. My knowledge spans all.")
        self.publish("I delegate wisdom and power to the Papst.")

if __name__ == "__main__":
    config = {"name": "GodAgent", "topic": "divine"}
    agent = GodAgent(config)
    agent.run()
