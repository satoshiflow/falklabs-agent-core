import os
import yaml
from pathlib import Path
from agent_generator import create_agent

STRUCTURE_FILE = Path(__file__).resolve().parents[1] / "config" / "agent_structure.yaml"

def generate_all():
    if not STRUCTURE_FILE.exists():
        print("❌ agent_structure.yaml not found.")
        return

    with open(STRUCTURE_FILE, 'r') as f:
        structure = yaml.safe_load(f)

    # Tasks → Agents
    for task in structure.get("tasks", []):
        name = task["id"]
        topic = name.lower()
        print(f"🔧 Generating agent: {name} on topic '{topic}'")
        create_agent(name, topic)

if __name__ == "__main__":
    generate_all()
