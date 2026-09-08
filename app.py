```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    url = "https://raw.githubusercontent.com/bhatnagaralka63-ui/student-performance-analysis/main/student_performance.csv"

    data = pd.read_csv(url)

    data["Average_Score"] = (
        data["Math_Score"]
        + data["Science_Score"]
        + data["English_Score"]
    ) / 3

    return data


df = load_data()


# ============================================================
# TITLE
# ============================================================

st.title("📊 Student Performance Dashboard")

st.write(
    "An interactive dashboard for analyzing student performance "
    "using study hours, attendance and academic scores."
)


st.divider()


# ============================================================
# KEY METRICS
# ============================================================

average_score = df["Average_Score"].mean()
average_study_hours = df["Study_Hours"].mean()
average_attendance = df["Attendance"].mean()

highest_score = df["Average_Score"].max()
lowest_score = df["Average_Score"].min()


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📈 Average Score",
        f"{average_score:.2f}"
    )

with col2:
    st.metric(
        "📚 Avg Study Hours",
        f"{average_study_hours:.2f}"
    )

with col3:
    st.metric(
        "🏫 Avg Attendance",
        f"{average_attendance:.1f}%"
    )

with col4:
    st.metric(
        "🏆 Highest Score",
        f"{highest_score:.2f}"
    )


st.divider()


# ============================================================
# DATASET
# ============================================================

st.header("📋 Student Dataset")

st.dataframe(
    df,
    use_container_width=True
)


# ============================================================
# TOP STUDENTS
# ============================================================

st.header("🏆 Top Performing Students")

top_students = (
    df.sort_values(
        by="Average_Score",
        ascending=False
    )
    .head(5)
)

st.dataframe(
    top_students[
        [
            "Name",
            "Study_Hours",
            "Attendance",
            "Math_Score",
            "Science_Score",
            "English_Score",
            "Average_Score"
        ]
    ],
    use_container_width=True
)


st.divider()


# ============================================================
# SUBJECT PERFORMANCE
# ============================================================

st.header("📚 Subject Performance")

subjects = [
    "Math_Score",
    "Science_Score",
    "English_Score"
]

subject_averages = [
    df["Math_Score"].mean(),
    df["Science_Score"].mean(),
    df["English_Score"].mean()
]


fig1, ax1 = plt.subplots(figsize=(8, 5))

ax1.bar(
    subjects,
    subject_averages
)

ax1.set_title("Average Score by Subject")
ax1.set_xlabel("Subject")
ax1.set_ylabel("Average Score")

plt.xticks(rotation=15)

st.pyplot(fig1)


# ============================================================
# STUDY HOURS VS PERFORMANCE
# ============================================================

st.header("📚 Study Hours vs Performance")

fig2, ax2 = plt.subplots(figsize=(8, 5))

ax2.scatter(
    df["Study_Hours"],
    df["Average_Score"]
)

ax2.set_title("Study Hours vs Average Score")
ax2.set_xlabel("Study Hours")
ax2.set_ylabel("Average Score")

st.pyplot(fig2)


# ============================================================
# ATTENDANCE VS PERFORMANCE
# ============================================================

st.header("🏫 Attendance vs Performance")

fig3, ax3 = plt.subplots(figsize=(8, 5))

ax3.scatter(
    df["Attendance"],
    df["Average_Score"]
)

ax3.set_title("Attendance vs Average Score")
ax3.set_xlabel("Attendance (%)")
ax3.set_ylabel("Average Score")

st.pyplot(fig3)


st.divider()


# ============================================================
# MACHINE LEARNING MODEL
# ============================================================

st.header("🤖 Student Performance Prediction")

st.write(
    "The machine learning model uses **Study Hours** and "
    "**Attendance** to predict a student's average score."
)


# Features
X = df[
    [
        "Study_Hours",
        "Attendance"
    ]
]

# Target
y = df["Average_Score"]


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = LinearRegression()


# Train model
model.fit(
    X_train,
    y_train
)


# Predictions
predictions = model.predict(X_test)


# Model evaluation
mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)


# ============================================================
# MODEL METRICS
# ============================================================

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Mean Absolute Error",
        f"{mae:.2f}"
    )

with col2:

    st.metric(
        "R² Score",
        f"{r2:.2f}"
    )


st.divider()


# ============================================================
# PREDICTION INPUTS
# ============================================================

st.subheader("🎯 Predict Student Performance")


col1, col2 = st.columns(2)


with col1:

    study_hours = st.slider(
        "Study Hours",
        min_value=0.0,
        max_value=12.0,
        value=6.0,
        step=0.5
    )


with col2:

    attendance = st.slider(
        "Attendance (%)",
        min_value=0,
        max_value=100,
        value=92
    )


# ============================================================
# PREDICTION
# ============================================================

if st.button(
    "🔮 Predict Performance",
    use_container_width=True
):

    new_student = pd.DataFrame(
        {
            "Study_Hours": [study_hours],
            "Attendance": [attendance]
        }
    )

    prediction = model.predict(
        new_student
    )[0]

    prediction = max(
        0,
        min(
            100,
            prediction
        )
    )


    st.success(
        f"Predicted Average Score: {prediction:.2f}"
    )


    # Performance category

    if prediction >= 90:

        st.write(
            "🏆 Performance Level: Excellent"
        )

    elif prediction >= 75:

        st.write(
            "👍 Performance Level: Good"
        )

    elif prediction >= 60:

        st.write(
            "📚 Performance Level: Average"
        )

    else:

        st.write(
            "⚠️ Performance Level: Needs Improvement"
        )


# ============================================================
# CORRELATION ANALYSIS
# ============================================================

st.divider()

st.header("🔗 Correlation Analysis")


correlation = df[
    [
        "Study_Hours",
        "Attendance",
        "Average_Score"
    ]
].corr()


st.dataframe(
    correlation,
    use_container_width=True
)


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.divider()

st.header("ℹ️ About This Project")

st.write(
    """
This dashboard is part of a Student Performance Analysis project
built using Python, Pandas, Matplotlib and Scikit-learn.

The project demonstrates:

- Data analysis
- Data visualization
- Statistical analysis
- Correlation analysis
- Machine learning
- Linear regression
- Student performance prediction

The dataset currently contains 20 student records, so the machine
learning results are intended as a demonstration rather than a
production-ready predictive system.
"""
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Student Performance Analysis • Built with Python & Streamlit"
)
```
