import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_performance.csv")

# -----------------------------
# BASIC DATASET INFORMATION
# -----------------------------

print("\n===== DATASET PREVIEW =====")
print(df.head())

print("\n===== DATASET INFORMATION =====")
print(df.info())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# -----------------------------
# AVERAGE PERFORMANCE
# -----------------------------

print("\n===== AVERAGE SCORES =====")

print("Average Math Score:",
      round(df["Math_Score"].mean(), 2))

print("Average Science Score:",
      round(df["Science_Score"].mean(), 2))

print("Average English Score:",
      round(df["English_Score"].mean(), 2))

# -----------------------------
# TOP PERFORMERS
# -----------------------------

df["Average_Score"] = (
    df["Math_Score"] +
    df["Science_Score"] +
    df["English_Score"]
) / 3

top_students = df.sort_values(
    by="Average_Score",
    ascending=False
).head(5)

print("\n===== TOP 5 STUDENTS =====")
print(
    top_students[
        ["Name", "Average_Score"]
    ]
)

# -----------------------------
# STUDY HOURS VS PERFORMANCE
# -----------------------------

print("\n===== STUDY HOURS ANALYSIS =====")

study_analysis = df.groupby(
    "Study_Hours"
)["Average_Score"].mean()

print(study_analysis)

# -----------------------------
# ATTENDANCE VS PERFORMANCE
# -----------------------------

print("\n===== ATTENDANCE ANALYSIS =====")

attendance_analysis = df.groupby(
    "Attendance"
)["Average_Score"].mean()

print(attendance_analysis)

# -----------------------------
# VISUALIZATION 1
# SUBJECT AVERAGES
# -----------------------------

subjects = [
    "Math_Score",
    "Science_Score",
    "English_Score"
]

averages = [
    df["Math_Score"].mean(),
    df["Science_Score"].mean(),
    df["English_Score"].mean()
]

plt.figure(figsize=(8, 5))

plt.bar(subjects, averages)

plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")

plt.tight_layout()
plt.show()

# -----------------------------
# VISUALIZATION 2
# STUDY HOURS VS SCORE
# -----------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Study_Hours"],
    df["Average_Score"]
)

plt.title("Study Hours vs Average Score")
plt.xlabel("Study Hours")
plt.ylabel("Average Score")

plt.tight_layout()
plt.show()

# -----------------------------
# VISUALIZATION 3
# ATTENDANCE VS SCORE
# -----------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Attendance"],
    df["Average_Score"]
)

plt.title("Attendance vs Average Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Score")

plt.tight_layout()
plt.show()

# -----------------------------
# CORRELATION
# -----------------------------

print("\n===== CORRELATION =====")

print(
    df[
        [
            "Study_Hours",
            "Attendance",
            "Average_Score"
        ]
    ].corr()
)

print("\n===== ANALYSIS COMPLETE =====")
