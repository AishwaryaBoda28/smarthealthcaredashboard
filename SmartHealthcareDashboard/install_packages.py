import subprocess
import sys

# Install all required packages
packages = [
    "flask-ngrok",
    "streamlit",
    "pyngrok",
    "scikit-learn",
    "pandas",
    "matplotlib",
    "plotly",
    "numpy",
    "dash",
]

for pkg in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "--quiet"])

print("✅ All packages installed successfully!")
