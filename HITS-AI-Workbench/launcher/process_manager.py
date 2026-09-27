import subprocess
import sys
import os
import time
from pathlib import Path
from core.logging import logger

class ProcessManager:
    def __init__(self):
        self.backend_process = None
        self.frontend_process = None
        self.root_dir = Path(__file__).resolve().parent.parent

    def start_backend(self):
        logger.info("Starting FastAPI Backend...")
        api_path = self.root_dir / "backend" / "api.py"
        try:
            self.backend_process = subprocess.Popen(
                [sys.executable, str(api_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=str(self.root_dir)
            )
            time.sleep(2) # Give it a moment to start
            if self.backend_process.poll() is not None:
                logger.error(f"Backend failed to start: {self.backend_process.stderr.read().decode()}")
                return False
            return True
        except Exception as e:
            logger.error(f"Failed to start backend: {e}")
            return False

    def start_frontend(self):
        logger.info("Starting Streamlit Frontend...")
        app_path = self.root_dir / "frontend" / "app.py"
        try:
            # Adding env variables if needed, specifying port
            env = os.environ.copy()
            self.frontend_process = subprocess.Popen(
                [sys.executable, "-m", "streamlit", "run", str(app_path), "--server.port=8501", "--server.headless=true"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=str(self.root_dir),
                env=env
            )
            time.sleep(2)
            if self.frontend_process.poll() is not None:
                logger.error(f"Frontend failed to start: {self.frontend_process.stderr.read().decode()}")
                return False
            return True
        except Exception as e:
            logger.error(f"Failed to start frontend: {e}")
            return False

    def stop_all(self):
        logger.info("Stopping all services...")
        if self.backend_process:
            self.backend_process.terminate()
        if self.frontend_process:
            self.frontend_process.terminate()
