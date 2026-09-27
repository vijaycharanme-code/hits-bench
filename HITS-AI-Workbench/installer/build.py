import subprocess
import sys
from pathlib import Path

def build_executable():
    root_dir = Path(__file__).resolve().parent.parent
    launcher_path = root_dir / "launcher" / "launcher.py"

    print("Building HITS-AI-Workbench.exe using PyInstaller...")
    try:
        subprocess.run([
            sys.executable, "-m", "PyInstaller",
            "--name", "HITS-AI-Workbench",
            "--onefile",
            "--clean",
            str(launcher_path)
        ], check=True, cwd=str(root_dir))
        print("Build complete! Check the 'dist' directory.")
    except Exception as e:
        print(f"Build failed: {e}")

if __name__ == "__main__":
    build_executable()
