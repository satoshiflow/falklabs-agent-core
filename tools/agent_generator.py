import os
import yaml
from pathlib import Path

AGENTS_YML = Path(__file__).resolve().parents[1] / "config" / "agents.yml"
AGENTS_DIR = Path(__file__).resolve().parents[1] / "agents"

TEMPLATE = """import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.base_agent import BaseAgent

class {class_name}(BaseAgent):
    def run(self):
        print(f"[{{self.name}}] Running {class_name} logic...")
        self.publish("{class_name} processed task")

if __name__ == "__main__":
    config = {{"name": "{class_name}", "topic": "{topic}"}}
    agent = {class_name}(config)
    agent.run()
"""

def to_snake_case(name):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in name]).lstrip('_')

def create_agent(name, topic):
    class_name = name[0].upper() + name[1:]
    folder_name = to_snake_case(name)
    agent_dir = AGENTS_DIR / folder_name
    agent_dir.mkdir(parents=True, exist_ok=True)

    with open(agent_dir / "main.py", "w") as f:
        f.write(TEMPLATE.format(class_name=class_name, topic=topic))

    if AGENTS_YML.exists():
        with open(AGENTS_YML, "r") as f:
            data = yaml.safe_load(f) or {}

        data.setdefault("agents", []).append({
            "name": class_name,
            "path": f"agents/{folder_name}"
        })

        with open(AGENTS_YML, "w") as f:
            yaml.dump(data, f)

    print(f"✅ Agent '{class_name}' created and registered.")
