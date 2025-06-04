import sys
from pathlib import Path

# Absoluter Pfad zum Projekt-Hauptverzeichnis (2 Ordner über dieser Datei)
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from shared.base_agent import BaseAgent

class CashbackAgent(BaseAgent):
    def run(self):
        print(f"[{self.name}] Running cashback logic...")
        self.publish("Cashback processed for user 123")

if __name__ == "__main__":
    agent_config = {"name": "CashbackAgent", "topic": "cashback"}
    agent = CashbackAgent(agent_config)
    agent.run()
