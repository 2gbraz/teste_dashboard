#!/usr/bin/env python3
"""
Launcher script for Execution Types Reference application
"""

import subprocess
import sys
import os

def main():
    """Run the Execution Types Reference Streamlit app"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(script_dir, "execution_types_reference.py")
    
    print("🎯 Starting Execution Types Reference...")
    print("📊 This application displays icon mappings for different execution types")
    print("🌐 Opening in your default browser...\n")
    
    try:
        subprocess.run([
            sys.executable,
            "-m",
            "streamlit",
            "run",
            app_path,
            "--server.headless=true"
        ])
    except KeyboardInterrupt:
        print("\n\n👋 Application stopped.")
    except Exception as e:
        print(f"❌ Error running application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


