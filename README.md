# 📊 Student Performance Analysis

A Python-based data analysis and machine learning project that explores how **study hours and attendance affect student academic performance**.

The project uses **Pandas, Matplotlib, and Scikit-learn** to analyze student data, visualize relationships, and build a machine learning model for predicting average student scores.

---

## 🚀 Project Overview

The goal of this project is to analyze student performance using factors such as:

* 📚 Study Hours
* 🏫 Attendance
* 📐 Mathematics Score
* 🔬 Science Score
* 📖 English Score

The project performs both **exploratory data analysis** and **machine learning prediction**.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** — Data manipulation and analysis
* **Matplotlib** — Data visualization
* **Scikit-learn** — Machine learning
* **Linear Regression** — Predicting student performance
* **Git & GitHub** — Version control and project hosting

---

## 📁 Project Structure

```text
student-performance-analysis/
│
├── analysis.py
├── ml_model.py
├── student_performance.csv
├── requirements.txt
└── README.md
```

### Files

| File                      | Description                                       |
| ------------------------- | ------------------------------------------------- |
| `analysis.py`             | Performs data analysis and creates visualizations |
| `ml_model.py`             | Trains and evaluates the machine learning model   |
| `student_performance.csv` | Student performance dataset                       |
| `requirements.txt`        | Required Python libraries                         |
| `README.md`               | Project documentation                             |

---

## 📊 Dataset

The dataset contains information about **20 students**.

### Columns

| Column          | Description             |
| --------------- | ----------------------- |
| `Name`          | Student name            |
| `Study_Hours`   | Number of hours studied |
| `Attendance`    | Attendance percentage   |
| `Math_Score`    | Mathematics score       |
| `Science_Score` | Science score           |
| `English_Score` | English score           |

An additional feature called `Average_Score` is calculated from the three subject scores.

```text
Average Score =
(Math Score + Science Score + English Score) / 3
```

---

## 🔍 Data Analysis

The `analysis.py` script performs several analyses.

### 1. Dataset Preview

Displays the first few records of the dataset.

### 2. Statistical Summary

Generates descriptive statistics using Pandas.

### 3. Average Subject Scores

Calculates the average:

* Mathematics score
* Science score
* English score

### 4. Top Performing Students

Calculates the average score for every student and identifies the top 5 performers.

### 5. Study Hours Analysis

Analyzes the relationship between study hours and average academic performance.

### 6. Attendance Analysis

Analyzes the relationship between attendance and average academic performance.

### 7. Correlation Analysis

Calculates correlations between:

* Study Hours
* Attendance
* Average Score

---

## 📈 Data Visualizations

The project generates three main visualizations.

### Average Score by Subject

Compares the average performance across Mathematics, Science, and English.

### Study Hours vs Average Score

A scatter plot showing the relationship between study time and academic performance.

### Attendance vs Average Score

A scatter plot showing how attendance relates to average student performance.

---

## 🤖 Machine Learning

The project also includes a machine learning model in `ml_model.py`.

### Model

**Linear Regression**

The model uses:

```text
Study Hours
Attendance
```

as input features.

The target variable is:

```text
Average Score
```

### Machine Learning Workflow

```text
Dataset
   ↓
Data Preparation
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Linear Regression
   ↓
Model Training
   ↓
Predictions
   ↓
Model Evaluation
```

---

## 🧪 Model Results

Using the current dataset and train/test split, the model produced:

```text
Mean Absolute Error: 0.31
R² Score: 0.99
```

The model was also used to predict the performance of a hypothetical student with:

```text
Study Hours: 6
Attendance: 92%
```

Predicted average score:

```text
88.63
```

> **Note:** The dataset contains only 20 records, so these metrics should be considered a demonstration of the machine learning workflow rather than evidence of a production-ready predictive model.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/bhatnagaralka63-ui/student-performance-analysis.git
```

### 2. Open the project

```bash
cd student-performance-analysis
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the data analysis

```bash
python analysis.py
```

### 5. Run the machine learning model

```bash
python ml_model.py
```

---

## 📦 Requirements

The project requires:

```text
pandas
matplotlib
scikit-learn
```

These dependencies are also included in `requirements.txt`.

---

## 💡 Key Insights

The analysis demonstrates how basic academic factors can be used to explore student performance.

Some noticeable patterns in the dataset include:

* Students with higher study hours generally achieve higher scores.
* Higher attendance generally corresponds with stronger academic performance.
* Study hours and attendance can be useful features for predicting average scores.
* Data visualization makes these relationships easier to understand.

Because the dataset is small and manually constructed, these observations should not be treated as statistically generalizable conclusions.

---

## 🔮 Future Improvements

Possible improvements include:

* Use a larger real-world student dataset
* Add more student features
* Compare multiple machine learning algorithms
* Add Random Forest regression
* Add Decision Tree regression
* Perform cross-validation
* Improve feature engineering
* Build an interactive dashboard
* Add model visualization
* Deploy the project as a web application
* Create a student performance prediction interface

---

## 🌐 Project

**GitHub Repository**

https://github.com/bhatnagaralka63-ui/student-performance-analysis

**Live Project Page**

https://bhatnagaralka63-ui.github.io/student-performance-analysis/

---

## 👨‍💻 Author

**Rudraksh Bhatnagar**

BCA — Data Science & AI

Interested in:

* Data Science
* Artificial Intelligence
* Machine Learning
* Python
* Software Development
* Data Analytics

---

## ⭐ Future Goal

This project is part of my journey toward building practical projects in **Data Science, Artificial Intelligence, and Machine Learning**.

More projects and improvements coming soon.

---

⭐ If you found this project useful, consider giving the repository a star!
