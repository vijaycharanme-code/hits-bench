import os
from pathlib import Path
from typing import Optional
from core.logging import logger
from core.exceptions import ModelLoadError
from core.config import MODELS_DIR, DEFAULT_LLM_MODEL, DEFAULT_EMBEDDING_MODEL

# We defer actual heavy model downloading logic to the `models` package
# This launcher level just ensures the right configuration is set up.

def select_model_for_profile(profile: str) -> str:
    """Selects the best model ID based on the hardware profile."""
    if profile == "PROFILE_1":
        # GPU with 16GB+ VRAM -> 7B or 8B model
        return "mistralai/Mistral-7B-Instruct-v0.2"
    elif profile == "PROFILE_2":
        # GPU with 8GB+ VRAM -> quantized or smaller model
        return "TheBloke/Mistral-7B-Instruct-v0.2-GGUF" # Example quantized
    else:
        # No GPU -> very lightweight
        return DEFAULT_LLM_MODEL

def prepare_models(profile: str):
    """Prepares necessary AI models."""
    logger.info("Preparing AI models...")
    llm_model = select_model_for_profile(profile)
    logger.info(f"Selected LLM for {profile}: {llm_model}")

    # In a real setup, we would trigger huggingface_hub downloads here.
    # We will simulate preparation to avoid huge downloads during setup unless running.

    # Verify/create cache dir
    cache_dir = MODELS_DIR / "cache"
    cache_dir.mkdir(exist_ok=True)

    logger.info("Models prepared (cached configuration setup).")
    return llm_model, DEFAULT_EMBEDDING_MODEL
