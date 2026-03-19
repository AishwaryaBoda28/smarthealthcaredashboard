===================================================
  Smart Healthcare Analytics Dashboard
===================================================

FILES IN THIS PROJECT:
-----------------------
  app.py           → Main Streamlit app (prediction + charts) — RUN THIS
  main.py          → Basic model training + plot (standalone script)
  model.py         → Model evaluation with accuracy, confusion matrix, report
  dashboard.py     → Dash-based visualization dashboard
  run_ngrok.py     → Launch app and expose via ngrok (optional/Colab use)
  requirements.txt → All required packages
  install_packages.py → Auto-installer script

HOW TO RUN:
-----------
Step 1: Install dependencies
    pip install -r requirements.txt

Step 2: Run the Streamlit app
    streamlit run app.py

Step 3: Open browser at
    http://localhost:8501

OTHER SCRIPTS:
--------------
  Run model evaluation only:
    python model.py

  Run basic training + plot:
    python main.py

  Run Dash dashboard:
    python dashboard.py
    → Opens at http://localhost:8050

NOTE:
-----
  run_ngrok.py is only needed if you want to share the app
  publicly via a URL (e.g., from Google Colab or a server).
  For local use, just run: streamlit run app.py
===================================================
