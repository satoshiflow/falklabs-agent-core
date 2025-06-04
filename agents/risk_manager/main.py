import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.base_agent import BaseAgent

class RiskManager(BaseAgent):
    def run(self):
        print(f"[{self.name}] Running RiskManager logic...")
        self.publish("RiskManager processed task")

if __name__ == "__main__":
    config = {"name": "RiskManager", "topic": "riskmanager"}
    agent = RiskManager(config)
    agent.run()
