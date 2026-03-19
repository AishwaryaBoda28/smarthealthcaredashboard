from pyngrok import ngrok
import subprocess
import time

# Start the Streamlit app
subprocess.Popen(["streamlit", "run", "app.py"])

# Authenticate ngrok
# Replace with your own authtoken from https://dashboard.ngrok.com
# ngrok.set_auth_token("YOUR_NGROK_AUTHTOKEN_HERE")

# Wait a moment and expose the app
time.sleep(5)
public_url = ngrok.connect(addr="8501")
print("🚀 App is live at:", public_url)
