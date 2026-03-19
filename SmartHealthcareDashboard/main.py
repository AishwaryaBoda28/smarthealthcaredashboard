import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Sample dataset
data = {
    "Pregnancies": [6, 1, 8, 1, 0],
    "Glucose": [148, 85, 183, 89, 137],
    "BloodPressure": [72, 66, 64, 66, 40],
    "SkinThickness": [35, 29, 0, 23, 35],
    "Insulin": [0, 0, 0, 94, 168],
    "BMI": [33.6, 26.6, 23.3, 28.1, 43.1],
    "DiabetesPedigreeFunction": [0.627, 0.351, 0.672, 0.167, 2.288],
    "Age": [50, 31, 32, 21, 33],
    "Outcome": [1, 0, 1, 0, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Split into features and target
x = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Plot actual vs predicted
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(range(len(y_test)), y_test.values, label='Actual', marker='o')
ax.plot(range(len(predictions)), predictions, label='Predicted', marker='x')
ax.set_title("Diabetes Prediction vs Actual")
ax.set_xlabel("Test Sample Index")
ax.set_ylabel("Outcome")
ax.legend()
plt.show()

# Display dataset and comparison
print("Dataset Head")
print(df.head())

print("\nPrediction vs Actuals:")
comparison_df = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})
print(comparison_df)
