import webbrowser
from core.logging import logger

def open_browser(port: int = 8501):
    url = f"http://127.0.0.1:{port}"
    logger.info(f"Opening browser at {url}")
    try:
        webbrowser.open(url)
    except Exception as e:
        logger.error(f"Failed to open browser: {e}")
