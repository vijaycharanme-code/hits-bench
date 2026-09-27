import platform
import psutil
import shutil
import subprocess
import json
from typing import Dict, Any

from core.logging import logger

def detect_os() -> str:
    return platform.system()

def detect_cpu() -> str:
    try:
        return platform.processor() or "Unknown CPU"
    except Exception:
        return "Unknown CPU"

def detect_ram() -> int:
    try:
        mem = psutil.virtual_memory()
        return round(mem.total / (1024 ** 3))
    except Exception:
        return 0

def get_nvidia_smi_info():
    """Helper to call nvidia-smi and return dict of info."""
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=name,memory.total,memory.free', '--format=csv,noheader,nounits'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        output = result.stdout.strip().split('\n')
        if output and output[0]:
            parts = [p.strip() for p in output[0].split(',')]
            if len(parts) >= 3:
                name = parts[0]
                total_vram_mb = int(parts[1])
                free_vram_mb = int(parts[2])
                return {
                    "name": name,
                    "total_vram_gb": round(total_vram_mb / 1024),
                    "free_vram_gb": round(free_vram_mb / 1024)
                }
    except Exception as e:
        logger.debug(f"nvidia-smi failed: {e}")
    return None

def detect_gpu() -> str:
    info = get_nvidia_smi_info()
    if info:
        return info["name"]
    return "None or Unsupported"

def detect_vram() -> int:
    info = get_nvidia_smi_info()
    if info:
        return info["total_vram_gb"]
    return 0

def detect_cuda() -> bool:
    try:
        result = subprocess.run(
            ['nvcc', '--version'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.returncode == 0
    except Exception:
        return False

def detect_disk_space() -> int:
    try:
        total, used, free = shutil.disk_usage("/")
        return round(free / (1024 ** 3))
    except Exception:
        return 0

def perform_system_check() -> Dict[str, Any]:
    """Runs all checks and returns a profile dict."""
    logger.info("Performing system check...")
    info = {
        "os": detect_os(),
        "cpu": detect_cpu(),
        "ram_gb": detect_ram(),
        "gpu": detect_gpu(),
        "vram_gb": detect_vram(),
        "cuda": detect_cuda(),
        "free_disk_gb": detect_disk_space()
    }

    # Determine profile
    if info["gpu"] != "None or Unsupported" and info["vram_gb"] >= 16:
        info["profile"] = "PROFILE_1" # GPU available + sufficient VRAM
    elif info["gpu"] != "None or Unsupported" and info["vram_gb"] >= 8:
        info["profile"] = "PROFILE_2" # GPU available + limited VRAM
    else:
        info["profile"] = "PROFILE_3" # No GPU

    logger.info(f"System check completed: {json.dumps(info)}")
    return info
