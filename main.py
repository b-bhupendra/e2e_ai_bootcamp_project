"""
End-to-End AI Bootcamp Project
Entry point and environment initialization script.
"""

import os
import sys
import platform
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()


def check_environment():
    print("=" * 60)
    print("🚀 End-to-End AI Bootcamp Project")
    print("=" * 60)
    print(f"Python Version : {sys.version.split()[0]}")
    print(f"Platform       : {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"Working Dir    : {Path.cwd()}")
    
    env_file = Path(".env")
    if env_file.exists():
        print(f"Config (.env)  : Loaded successfully")
    else:
        print(f"Config (.env)  : Not found (copy .env.example to .env if needed)")
    print("-" * 60)
    print("AI pipeline environment initialized successfully!")
    print("=" * 60)


if __name__ == "__main__":
    check_environment()
