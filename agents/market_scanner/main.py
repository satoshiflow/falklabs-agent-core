import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.base_agent import BaseAgent

class MarketScanner(BaseAgent):
    def run(self):
        print(f"[{self.name}] Running MarketScanner logic...")
        self.publish("MarketScanner processed task")

if __name__ == "__main__":
    config = {"name": "MarketScanner", "topic": "marketscanner"}
    agent = MarketScanner(config)
    agent.run()
