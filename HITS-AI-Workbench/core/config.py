import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
MODELS_DIR = BASE_DIR / "models"
DB_DIR = BASE_DIR / "database"

# Ensure directories exist
for _dir in [DATA_DIR, LOGS_DIR, MODELS_DIR, DB_DIR]:
    _dir.mkdir(parents=True, exist_ok=True)

# Versioning
VERSION = "1.0.0"

# Application Config
APP_NAME = "HITS AI Workbench"
DEFAULT_PORT = 8501
BACKEND_PORT = 8000

# Hardware Fallbacks
USE_GPU_IF_AVAILABLE = True

# Models
# Define fallback models
DEFAULT_LLM_MODEL = "Qwen/Qwen2.5-Coder-0.5B-Instruct" # Updated as requested
DEFAULT_EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Security
ALLOW_EXTERNAL_API = False

# LangGraph limits
MAX_RETRIES = 3
