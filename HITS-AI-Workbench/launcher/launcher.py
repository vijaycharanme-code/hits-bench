import sys
import time
from core.logging import logger
from launcher.system_check import perform_system_check
from launcher.dependency_manager import setup_environment
from launcher.model_manager import prepare_models
from launcher.process_manager import ProcessManager
from launcher.browser_manager import open_browser

def main():
    print("\n=========================================")
    print("        HITS AI WORKBENCH        ")
    print("=========================================\n")
    print("Initializing secure local AI environment...\n")

    print("[1/8] Checking operating system and hardware...")
    hw_info = perform_system_check()

    print(f"[2/8] Preparing Python environment...")
    setup_environment(minimal=False)

    print(f"[3/8] Preparing AI models for {hw_info['profile']}...")
    prepare_models(hw_info['profile'])

    print("[4/8] Starting services...")
    pm = ProcessManager()

    if not pm.start_backend():
        print("CRITICAL: Failed to start backend.")
        sys.exit(1)

    print("[5/8] Starting UI...")
    if not pm.start_frontend():
        print("CRITICAL: Failed to start frontend.")
        pm.stop_all()
        sys.exit(1)

    print("[6/8] System Online!")
    open_browser()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down HITS AI Workbench...")
        pm.stop_all()
        sys.exit(0)

if __name__ == "__main__":
    main()
