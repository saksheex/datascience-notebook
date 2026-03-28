# datascience-notebook


 # 📊 Python Data Analysis Projects

> Data analysis and visualization projects using real-world datasets — COVID-19 India statistics and Student Lifestyle & Academic Performance.

---

## 📋 Table of Contents

- [About](#about)
- [Datasets Used](#datasets-used)
- [Projects](#projects)
  - [Project 1 — COVID-19 State-wise Lookup](#project-1--covid-19-state-wise-lookup)
  - [Project 2 — COVID-19 Regression Analysis](#project-2--covid-19-regression-analysis)
  - [Project 3 — Student Risk Index Analysis](#project-3--student-risk-index-analysis)
- [Technologies Used](#technologies-used)
- [How to Run](#how-to-run)

---

## About

This repository contains three Python data analysis programs built on two real-world CSV datasets. The projects explore COVID-19 case distribution across Indian states and student lifestyle patterns that may indicate academic burnout risk.

---

## Datasets Used

### 🦠 `Latest Covid-19 India Status.csv`

State/UT-wise COVID-19 statistics across India.

| Column | Description |
|--------|-------------|
| `State/UTs` | Name of the Indian state or union territory |
| `Total Cases` | Total confirmed COVID-19 cases |
| `Active` | Currently active cases |
| `Discharged` | Total recovered/discharged patients |
| `Deaths` | Total deaths reported |
| `Active Ratio` | Percentage of active cases |
| `Discharge Ratio` | Percentage of discharged cases |
| `Death Ratio` | Percentage of deaths |
| `Population` | State population |

---

### 🎓 `student_lifestyle_performance_dataset.csv`

Academic and lifestyle data of college students across branches.

| Column | Description |
|--------|-------------|
| `Age` | Age of the student |
| `Branch` | Engineering branch (CSE, ECE, Civil, etc.) |
| `Study_Hours_per_Day` | Daily study hours |
| `Sleep_Hours` | Daily sleep hours |
| `Screen_Time_Hours` | Daily screen time hours |
| `Gym_Hours_per_Week` | Weekly gym hours |
| `Diet_Type` | Veg / Non-Veg |
| `Attendance_Percentage` | Class attendance percentage |
| `Stress_Level_1_to_10` | Self-reported stress level (1–10) |
| `Residence` | Hosteller / Day Scholar |
| `Internal_Marks` | Internal assessment marks |
| `CGPA` | Cumulative Grade Point Average |

---

## Projects

---

### Project 1 — COVID-19 State-wise Lookup

**File:** `covid_lookup.py`

#### 📌 Description

An **interactive program** that lets the user enter any Indian state name and instantly see a detailed breakdown of COVID-19 statistics for that state, along with a **pie chart visualization**.

#### ⚙️ How it works

1. Loads `Latest Covid-19 India Status.csv` using `pandas`
2. Prompts the user to enter a state name (case-insensitive)
3. Filters the dataset for the matching state
4. Prints a summary of Total Cases, Active, Discharged, and Deaths
5. Generates a **pie chart** with a legend showing exact numbers

#### 🖥️ Sample Output

```
Enter the state name of your preference: maharashtra

State        : Maharashtra
Total Cases  : 7,907,923
Active       : 0
Discharged   : 7,755,092
Deaths       : 143,575
```

A pie chart is then displayed showing the **percentage distribution** of:
- 🔴 Total Cases
- 🟢 Active Cases
- 🔵 Discharged
- ⚫ Deaths

#### 📊 Visualization

The pie chart includes:
- Color-coded slices (Red, Green, Blue, Black)
- Percentage labels on each slice
- A legend with exact case counts
- Bold title: `COVID-19 Distribution for {State}`

---

### Project 2 — COVID-19 Regression Analysis

**File:** `covid_regression.py`

#### 📌 Description

Performs **exploratory data analysis (EDA)** on the COVID-19 dataset and plots a **regression plot** showing the relationship between Total Cases and Active Cases across all Indian states.

#### ⚙️ How it works

1. Loads the CSV and prints the first 5 rows with `df.head()`
2. Checks for missing values with `df.isna().sum()`
3. Plots a **regression line** using `seaborn.regplot` between:
   - X-axis: `Total Cases`
   - Y-axis: `Active Cases`

#### 📊 Visualization

A scatter plot with a **fitted regression line** showing:
- How active cases scale with total cases
- Outlier states with unusually high or low active ratios
- Figure size: 12 × 6 for clear readability

**Chart title:** `Total cases v/s Active cases`

---

### Project 3 — Student Risk Index Analysis

**File:** `student_risk.py`

#### 📌 Description

Computes a custom **Risk Index** for each student to identify those most at risk of **academic burnout or low grades**, then displays the top 5 highest-risk students.

#### ⚙️ Risk Index Formula

```
Risk_Index = (Stress_Level / 10) - (Attendance_Percentage / 100) - (Sleep_Hours / 10)
```

| Component | Effect on Risk |
|-----------|---------------|
| Higher Stress Level | ⬆️ Increases risk |
| Higher Attendance | ⬇️ Decreases risk |
| More Sleep | ⬇️ Decreases risk |

Students are sorted by `Risk_Index` in **descending order** and the top 5 at-risk students are displayed.

#### 🖥️ Sample Output

```
   Branch     CGPA  Stress_Level_1_to_10  Risk_Index
   ECE        4.21          9.5             0.712
   Electrical 3.84          8.9             0.681
   Civil      5.10          9.1             0.654
   CSE        4.67          8.7             0.643
   ECE        4.33          9.0             0.631
```

#### 💡 Insight

Students with **high stress, low attendance, and poor sleep** bubble to the top — making this a practical early-warning tool for academic counselors.

---

## Technologies Used

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading, filtering, and manipulation |
| `numpy` | Numerical operations |
| `matplotlib` | Pie charts and plot customization |
| `seaborn` | Regression plot visualization |

---

## How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/data-analysis-projects.git
cd data-analysis-projects
```

**2. Install dependencies:**
```bash
pip install pandas numpy matplotlib seaborn
```

**3. Make sure both CSV files are in the same folder:**
```
📁 project-folder/
├── covid_lookup.py
├── covid_regression.py
├── student_risk.py
├── Latest Covid-19 India Status.csv
└── student_lifestyle_performance_dataset.csv
```

**4. Run each project:**
```bash
# Project 1 - Interactive COVID lookup + pie chart
python covid_lookup.py

# Project 2 - COVID regression analysis
python covid_regression.py

# Project 3 - Student risk index
python student_risk.py
```

---

## 📁 Project Structure

```
📁 data-analysis-projects/
│
├── 📄 covid_lookup.py           # Project 1: State-wise COVID lookup + pie chart
├── 📄 covid_regression.py       # Project 2: Total vs Active cases regression
├── 📄 student_risk.py           # Project 3: Student burnout risk analysis
│
├── 📊 Latest Covid-19 India Status.csv
├── 📊 student_lifestyle_performance_dataset.csv
│
└── 📘 README.md
```

---

> *Built with Python 🐍 | Data tells the story 📊*

