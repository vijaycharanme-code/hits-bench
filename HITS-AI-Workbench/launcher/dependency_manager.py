import os
import json
import subprocess
import sys
from pathlib import Path
from core.logging import logger
from core.exceptions import DependencyInstallationError
from core.config import DATA_DIR

STATE_FILE = DATA_DIR / "install_state.json"

def get_installed_state() -> dict:
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_installed_state(state: dict):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def check_and_install_dependencies(requirements_file: Path):
    if not requirements_file.exists():
        logger.error(f"Requirements file not found: {requirements_file}")
        return

    logger.info(f"Checking dependencies from {requirements_file}...")
    state = get_installed_state()

    with open(requirements_file, "r") as f:
        packages = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    for pkg in packages:
        # Simple extraction of package name (ignoring version for simple state tracking)
        pkg_name = pkg.split("==")[0].split(">=")[0].strip()

        if state.get(pkg_name) == pkg:
            logger.debug(f"Package {pkg} already installed according to state.")
            continue

        logger.info(f"Installing {pkg}...")
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", pkg],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            logger.info(f"Successfully installed {pkg}")
            state[pkg_name] = pkg
            save_installed_state(state)
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to install {pkg}: {e.stderr}")
            raise DependencyInstallationError(f"Failed to install {pkg}") from e

def setup_environment(minimal: bool = False):
    """Installs required dependencies."""
    req_file = "requirements-minimal.txt" if minimal else "requirements.txt"
    req_path = Path(__file__).resolve().parent.parent / req_file
    check_and_install_dependencies(req_path)
