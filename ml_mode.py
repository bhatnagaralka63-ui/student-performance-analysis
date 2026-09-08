import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset directly from GitHub
url =  "https://raw.githubusercontent.com/bhatnagaralka63-ui/student-performance-analysis/main/student_performance.csv"

df = pd.read_csv(url)

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

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Model evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("===== MODEL RESULTS =====")
print("Mean Absolute Error:", round(mae, 2))
print("R² Score:", round(r2, 2))

# Example prediction
study_hours = 6
attendance = 92

new_student = pd.DataFrame({
    "Study_Hours": [study_hours],
    "Attendance": [attendance]
})

prediction = model.predict(new_student)

print("\n===== STUDENT PREDICTION =====")
print("Study Hours:", study_hours)
print("Attendance:", attendance)
print("Predicted Average Score:", round(prediction[0], 2))
