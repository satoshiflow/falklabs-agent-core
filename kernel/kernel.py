import yaml
import subprocess
from pathlib import Path

def load_agents_config(path):
    try:
        with open(path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"❌ Fehler beim Laden der Konfiguration: {e}")
        return {}

def spawn_agents(agent_defs):
    root_dir = Path(__file__).resolve().parent.parent  # <== wichtig!
    for agent in agent_defs.get("agents", []):
        path = Path(agent["path"])
        print(f"🚀 Starte Agent: {agent['name']}...")
        subprocess.Popen(
            [".venv\\Scripts\\python.exe", str(path / "main.py")],
            cwd=root_dir  # <-- hier wird im richtigen Verzeichnis gestartet
        )

if __name__ == "__main__":
    config = load_agents_config("config/agents.yml")
    spawn_agents(config)
# This script loads agent configurations from a YAML file and spawns each agent as a separate process.
# It uses the `subprocess` module to run each agent's main script in a new process.