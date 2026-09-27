import pytest
from launcher.system_check import perform_system_check, detect_os, detect_cpu

def test_detect_os():
    os_name = detect_os()
    assert isinstance(os_name, str)
    assert len(os_name) > 0

def test_perform_system_check():
    info = perform_system_check()
    assert "os" in info
    assert "cpu" in info
    assert "ram_gb" in info
    assert "gpu" in info
    assert "profile" in info
    assert info["profile"] in ["PROFILE_1", "PROFILE_2", "PROFILE_3"]
