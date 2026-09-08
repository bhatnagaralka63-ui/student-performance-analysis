import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 {
    font-size: 42px !important;
    font-weight: 700 !important;
}

h2 {
    font-weight: 650 !important;
}

h3 {
    font-weight: 600 !important;
}

[data-testid="stMetric"] {
    background: #161b22;
    border: 1px solid #30363d;
    padding: 20px;
    border-radius: 14px;
}

[data-testid="stMetricValue"] {
    font-size: 28px;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


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
# SIDEBAR
# ============================================================

st.sidebar.title("🎛️ Dashboard Controls")

st.sidebar.subheader("Filters")

min_hours = float(df["Study_Hours"].min())
max_hours = float(df["Study_Hours"].max())

study_filter = st.sidebar.slider(
    "Study Hours",
    min_value=min_hours,
    max_value=max_hours,
    value=(min_hours, max_hours),
    step=0.5
)

attendance_filter = st.sidebar.slider(
    "Attendance (%)",
    min_value=int(df["Attendance"].min()),
    max_value=int(df["Attendance"].max()),
    value=(
        int(df["Attendance"].min()),
        int(df["Attendance"].max())
    )
)

filtered_df = df[
    (df["Study_Hours"] >= study_filter[0])
    & (df["Study_Hours"] <= study_filter[1])
    & (df["Attendance"] >= attendance_filter[0])
    & (df["Attendance"] <= attendance_filter[1])
]


# ============================================================
# HEADER
# ============================================================

st.title("📊 Student Performance Analytics")

st.write(
    "Interactive analysis of student performance using "
    "study hours, attendance, academic scores and machine learning."
)

st.divider()


# ============================================================
# KEY METRICS
# ============================================================

if len(filtered_df) > 0:

    average_score = filtered_df["Average_Score"].mean()
    average_study = filtered_df["Study_Hours"].mean()
    average_attendance = filtered_df["Attendance"].mean()
    highest_score = filtered_df["Average_Score"].max()

else:

    average_score = 0
    average_study = 0
    average_attendance = 0
    highest_score = 0


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📈 Average Score",
        f"{average_score:.2f}"
    )

with col2:
    st.metric(
        "📚 Avg Study Hours",
        f"{average_study:.2f}"
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
# FILTERED DATA
# ============================================================

st.header("👨‍🎓 Student Records")

st.write(
    f"Showing **{len(filtered_df)}** students based on your filters."
)

st.dataframe(
    filtered_df[
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
    use_container_width=True,
    hide_index=True
)


# ============================================================
# TOP STUDENTS
# ============================================================

st.header("🏆 Top Performing Students")

top_students = (
    filtered_df
    .sort_values(
        by="Average_Score",
        ascending=False
    )
    .head(5)
)

if len(top_students) > 0:

    st.dataframe(
        top_students[
            [
                "Name",
                "Study_Hours",
                "Attendance",
                "Average_Score"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No students match the selected filters.")


st.divider()


# ============================================================
# SUBJECT PERFORMANCE
# ============================================================

st.header("📚 Subject Performance")

subjects = [
    "Math",
    "Science",
    "English"
]

subject_averages = [
    filtered_df["Math_Score"].mean(),
    filtered_df["Science_Score"].mean(),
    filtered_df["English_Score"].mean()
]

if len(filtered_df) > 0:

    fig1, ax1 = plt.subplots(figsize=(9, 5))

    ax1.bar(
        subjects,
        subject_averages
    )

    ax1.set_title(
        "Average Score by Subject"
    )

    ax1.set_xlabel("Subject")
    ax1.set_ylabel("Average Score")

    ax1.set_ylim(0, 100)

    st.pyplot(
        fig1,
        use_container_width=True
    )


# ============================================================
# STUDY HOURS VS PERFORMANCE
# ============================================================

st.header("📚 Study Hours vs Performance")

if len(filtered_df) > 0:

    fig2, ax2 = plt.subplots(figsize=(9, 5))

    ax2.scatter(
        filtered_df["Study_Hours"],
        filtered_df["Average_Score"]
    )

    ax2.set_title(
        "Study Hours vs Average Score"
    )

    ax2.set_xlabel("Study Hours")
    ax2.set_ylabel("Average Score")

    ax2.set_ylim(0, 100)

    st.pyplot(
        fig2,
        use_container_width=True
    )


# ============================================================
# ATTENDANCE VS PERFORMANCE
# ============================================================

st.header("🏫 Attendance vs Performance")

if len(filtered_df) > 0:

    fig3, ax3 = plt.subplots(figsize=(9, 5))

    ax3.scatter(
        filtered_df["Attendance"],
        filtered_df["Average_Score"]
    )

    ax3.set_title(
        "Attendance vs Average Score"
    )

    ax3.set_xlabel("Attendance (%)")
    ax3.set_ylabel("Average Score")

    ax3.set_ylim(0, 100)

    st.pyplot(
        fig3,
        use_container_width=True
    )


st.divider()


# ============================================================
# CORRELATION
# ============================================================

st.header("🔗 Correlation Analysis")

correlation = df[
    [
        "Study_Hours",
        "Attendance",
        "Average_Score"
    ]
].corr()

st.dataframe(
    correlation.round(3),
    use_container_width=True
)


# ============================================================
# MACHINE LEARNING MODEL
# ============================================================

st.divider()

st.header("🤖 Machine Learning Prediction")

st.write(
    "A Linear Regression model predicts Average Score "
    "using Study Hours and Attendance."
)


X = df[
    [
        "Study_Hours",
        "Attendance"
    ]
]

y = df["Average_Score"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = LinearRegression()

model.fit(
    X_train,
    y_train
)


predictions = model.predict(
    X_test
)


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

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "MAE",
        f"{mae:.2f}"
    )

with col2:

    st.metric(
        "R² Score",
        f"{r2:.2f}"
    )

with col3:

    st.metric(
        "Training Records",
        len(X_train)
    )


st.divider()


# ============================================================
# PREDICTION
# ============================================================

st.subheader("🎯 Predict Student Performance")

col1, col2 = st.columns(2)

with col1:

    prediction_hours = st.slider(
        "Study Hours",
        0.0,
        12.0,
        6.0,
        0.5
    )

with col2:

    prediction_attendance = st.slider(
        "Attendance (%)",
        0,
        100,
        90
    )


if st.button(
    "🔮 Predict Performance"
):

    new_student = pd.DataFrame(
        {
            "Study_Hours": [prediction_hours],
            "Attendance": [prediction_attendance]
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
# AUTOMATIC INSIGHTS
# ============================================================

st.divider()

st.header("💡 Key Insights")

if len(df) > 0:

    best_student = df.loc[
        df["Average_Score"].idxmax()
    ]

    highest_study_student = df.loc[
        df["Study_Hours"].idxmax()
    ]

    highest_attendance_student = df.loc[
        df["Attendance"].idxmax()
    ]

    st.write(
        f"🏆 **Top performer:** {best_student['Name']} "
        f"with an average score of "
        f"**{best_student['Average_Score']:.2f}**."
    )

    st.write(
        f"📚 **Highest study time:** "
        f"{highest_study_student['Name']} "
        f"with {highest_study_student['Study_Hours']} study hours."
    )

    st.write(
        f"🏫 **Highest attendance:** "
        f"{highest_attendance_student['Name']} "
        f"with {highest_attendance_student['Attendance']}% attendance."
    )

    study_correlation = df[
        "Study_Hours"
    ].corr(
        df["Average_Score"]
    )

    attendance_correlation = df[
        "Attendance"
    ].corr(
        df["Average_Score"]
    )

    st.write(
        f"📈 **Study Hours correlation:** "
        f"{study_correlation:.2f}"
    )

    st.write(
        f"📊 **Attendance correlation:** "
        f"{attendance_correlation:.2f}"
    )


# ============================================================
# ABOUT
# ============================================================

st.divider()

st.header("ℹ️ About This Project")

st.write(
    """
This project demonstrates a complete beginner-level
Data Science workflow:

• Data collection
• Data cleaning
• Exploratory Data Analysis
• Statistical analysis
• Data visualization
• Correlation analysis
• Machine Learning
• Linear Regression
• Interactive prediction
• Streamlit dashboard development

The dataset currently contains 20 student records.

The machine learning results are intended for demonstration
and learning purposes rather than real-world deployment.
"""
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Student Performance Analysis • Python • Pandas • Matplotlib • Scikit-learn • Streamlit"
)
