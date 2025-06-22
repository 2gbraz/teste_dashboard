#!/usr/bin/env python3
"""
Quick start script for the Financial Dashboard
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'streamlit',
        'pandas',
        'plotly',
        'gspread',
        'google-auth'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Install them with:")
        print("   pip install -r requirements.txt")
        return False
    
    return True

def main():
    print("🚀 Financial Dashboard - Quick Start")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("✅ All dependencies are installed!")
    print("\n📋 Next steps:")
    print("1. Set up Google Sheets connection (see README.md)")
    print("2. Place your service_account_key.json in this directory")
    print("3. Share your Google Sheet with the service account email")
    print("\n🎯 For now, the dashboard will run with sample data")
    
    # Check if service account key exists
    if not os.path.exists('service_account_key.json'):
        print("\n⚠️  No service_account_key.json found")
        print("   The dashboard will use sample data for demonstration")
    
    print("\n🌐 Starting dashboard...")
    print("   The dashboard will open in your browser at http://localhost:8501")
    print("   Press Ctrl+C to stop the dashboard")
    print("\n" + "=" * 50)
    
    try:
        # Run the dashboard
        subprocess.run([sys.executable, "-m", "streamlit", "run", "financial_dashboard.py"])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error starting dashboard: {e}")

if __name__ == "__main__":
    main() 