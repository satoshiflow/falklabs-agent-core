import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.base_agent import BaseAgent

class TokenBuilder(BaseAgent):
    def run(self):
        print(f"[{self.name}] Running TokenBuilder logic...")
        self.publish("TokenBuilder processed task")

if __name__ == "__main__":
    config = {"name": "TokenBuilder", "topic": "tokenbuilder"}
    agent = TokenBuilder(config)
    agent.run()
