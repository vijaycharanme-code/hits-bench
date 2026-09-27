import pytest
from launcher.model_manager import select_model_for_profile

def test_model_fallback():
    model1 = select_model_for_profile("PROFILE_1")
    model2 = select_model_for_profile("PROFILE_2")
    model3 = select_model_for_profile("PROFILE_3")

    assert model1 != model3
    # PROFILE_3 should select the default lightweight model
    assert "qwen" in model3.lower() or "tinyllama" in model3.lower() or "lightweight" in model3.lower() or "huggingface" in model3.lower()
