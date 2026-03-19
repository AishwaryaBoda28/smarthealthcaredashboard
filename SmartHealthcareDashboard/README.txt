# 🩺 Smart Healthcare Analytics Dashboard

A machine learning–powered web application for diabetes prediction and healthcare data visualization. Built with Python, Streamlit, and scikit-learn.

---

## 📌 Overview

This project provides an interactive dashboard that allows users to:

- Input patient health metrics and receive a **diabetes risk prediction**
- Explore **data visualizations** including outcome distributions, glucose levels, and age analysis
- Evaluate the underlying **Random Forest classification model**

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/smart-healthcare-dashboard.git
cd smart-healthcare-dashboard

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run app.py
```

Then open your browser at **http://localhost:8501**

---

## 📁 Project Structure

```
├── app.py                  # Main Streamlit app — prediction + charts (START HERE)
├── main.py                 # Standalone model training + visualization script
├── model.py                # Model evaluation: accuracy, confusion matrix, report
├── dashboard.py            # Dash-based analytics dashboard
├── run_ngrok.py            # Expose app publicly via ngrok (optional)
├── install_packages.py     # Auto-installs all required packages
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🧠 Features

### Prediction
Enter patient data through the sidebar form and instantly get a prediction:
- ✅ **Unlikely to have diabetes**
- ⚠️ **Likely to have diabetes**

### Visualizations
- 📊 Outcome distribution (Diabetic vs Non-Diabetic)
- 👵 Age vs Outcome bar chart
- 🍬 Glucose level histogram
- 📋 Raw data table viewer

### Model
- Algorithm: **Random Forest Classifier**
- Preprocessing: **StandardScaler** normalization
- Features: Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age

---

## 🛠 Other Scripts

| Script | Command | Description |
|---|---|---|
| Model evaluation | `python model.py` | Prints accuracy, confusion matrix, classification report |
| Basic training + plot | `python main.py` | Trains model and plots predicted vs actual |
| Dash dashboard | `python dashboard.py` | Opens alternate viz dashboard at `http://localhost:8050` |
| Auto-install packages | `python install_packages.py` | Installs all dependencies automatically |

---

## ☁️ Public Deployment (Optional)

To expose the app via a public URL (useful for Google Colab or remote servers):

1. Get your free authtoken from [ngrok dashboard](https://dashboard.ngrok.com)
2. Add it to `run_ngrok.py`
3. Run:

```bash
python run_ngrok.py
```

---

## 📦 Dependencies

```
streamlit
pandas
numpy
scikit-learn
matplotlib
plotly
dash
pyngrok
flask-ngrok
```

---

## 📊 Dataset

The app currently uses a sample subset of the [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database). Replace the inline `data` dictionary in `app.py` or `model.py` with your full dataset for production use.

---

## ⚠️ Disclaimer

This tool is for **educational and demonstration purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

[MIT](LICENSE)
