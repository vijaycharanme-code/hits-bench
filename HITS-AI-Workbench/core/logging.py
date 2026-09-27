import logging
import sys
from logging.handlers import RotatingFileHandler
from core.config import LOGS_DIR

def setup_logger(name: str, log_file: str = "app.log", level=logging.INFO) -> logging.Logger:
    """Sets up a logger with console and file handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding handlers multiple times if logger is already configured
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Console Handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        # File Handler
        file_path = LOGS_DIR / log_file
        fh = RotatingFileHandler(file_path, maxBytes=10*1024*1024, backupCount=5)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger

# Default logger for easy import
logger = setup_logger("HITS-AI")
