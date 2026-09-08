import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("student_performance.csv")

# Create average score
df["Average_Score"] = (
    df["Math_Score"] +
    df["Science_Score"] +
    df["English_Score"]
) / 3

# Features
X = df[["Study_Hours", "Attendance"]]

# Target
y = df["Average_Score"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Machine Learning model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("===== MODEL RESULTS =====")
print("Mean Absolute Error:", round(mae, 2))
print("R² Score:", round(r2, 2))

# Predict a new student's performance
study_hours = 6
attendance = 92

prediction = model.predict(
    [[study_hours, attendance]]
)

print("\n===== NEW STUDENT PREDICTION =====")
print("Study Hours:", study_hours)
print("Attendance:", attendance)
print(
    "Predicted Average Score:",
    round(prediction[0], 2)
)
