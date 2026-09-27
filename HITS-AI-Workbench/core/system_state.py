from typing import Dict, Any, Optional

class SystemState:
    """Singleton to hold the application's current state."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SystemState, cls).__new__(cls)
            cls._instance._init_state()
        return cls._instance

    def _init_state(self):
        self.hardware_info: Dict[str, Any] = {}
        self.status: str = "INITIALIZING"
        self.active_models: Dict[str, Any] = {}
        self.backend_ready: bool = False
        self.agents_ready: bool = False
        self.ui_ready: bool = False

    def update_hardware_info(self, info: Dict[str, Any]):
        self.hardware_info = info

    def get_hardware_info(self) -> Dict[str, Any]:
        return self.hardware_info

    def set_status(self, status: str):
        self.status = status

    def get_status(self) -> str:
        return self.status

# Global instance
state = SystemState()
