# 🌍 Global Weather Analyzer

> A data analysis project exploring global weather patterns using Python — built from scratch with Pandas, NumPy and Matplotlib.

---

## 📖 About the Project

Weather affects everything around us — from what we wear to how we travel. This project dives deep into real world global weather data to uncover patterns, trends and insights from hundreds of cities across the world using Python.

Built completely from scratch using **Pandas, NumPy and Matplotlib** — no shortcuts, no automation — just pure data analysis!

---

## 📋 Dataset

| Property | Details |
|---|---|
| **Source** | Kaggle — Global Weather Repository |
| **Link** | [Global Weather Repository](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository) |
| **Size** | 47,000+ rows, 35+ columns |
| **Updates** | Daily |
| **Data includes** | Temperature, Humidity, Wind Speed, Air Quality, Sunrise/Sunset, Weather Conditions and more |

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---|---|---|
| `Python` | 3.x | Core language |
| `Pandas` | Latest | Loading, filtering, grouping and exploring data |
| `NumPy` | Latest | Math, correlation, absolute difference calculations |
| `Matplotlib` | Latest | Data visualizations and charts |

---

## ✅ What This Project Covers

### 🟢 Level 1 — Data Loading & Exploration
- ✅ Loaded dataset using Pandas and displayed first 10 rows
- ✅ Found total number of rows and columns using `df.shape`
- ✅ Displayed all column names and their data types
- ✅ Found total number of unique countries using `nunique()`
- ✅ Checked for missing values in each column
- ✅ Displayed basic statistics (mean, min, max, std) for all numeric columns
- ✅ Filtered dataset for 3 countries and printed their data
- ✅ Found top 5 hottest and top 5 coldest countries by average temperature

### 🟡 Level 2 — Pandas + NumPy Analysis
- ✅ Calculated average temperature, humidity and wind speed per country using `groupby()`
- ✅ Found correlation between `temperature_celsius` and `feels_like_celsius` using `np.corrcoef()`
- ✅ Found cities where temperature and feels-like differ the most using `np.abs()`
- ✅ Calculated day length (sunset - sunrise) and added it as a new column
- ✅ Found most common weather condition globally using `value_counts()`
- ✅ Found top 10 most polluted cities based on `air_quality_PM2.5`
- ✅ Created `temp_category` column using `np.where()` — labelled each row as `Hot`, `Mild` or `Cold`
- ✅ Found most common wind direction globally

---

## 📊 Key Insights

- 🌡️ Found the hottest and coldest countries in the world by average temperature
- 💧 Temperature and feels-like temperature have a very strong correlation — they almost always move together
- 🌫️ Identified the top 10 most polluted cities in the world using PM2.5 air quality index
- 🌅 Calculated exact day length for every city by subtracting sunrise from sunset
- 💨 Analysed the most common wind directions across all cities globally
- 🏷️ Categorised every city as Hot, Mild or Cold based on temperature thresholds

---

## 🚀 How to Run

**Step 1 — Clone the repository**
```bash
git clone https://github.com/saksheex/datascience-notebook.git
cd datascience-notebook/global-weather-analyzer
```

**Step 2 — Install required libraries**
```bash
pip install pandas numpy matplotlib
```

**Step 3 — Download the dataset**
- Download `GlobalWeatherRepository.csv` from [Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository)
- Place it inside the `global-weather-analyzer/` folder

**Step 4 — Run the script**
```bash
python live_global_weather.py
```

---

## 📁 Project Structure

```
global-weather-analyzer/
│
├── live_global_weather.py       ← main analysis script
├── GlobalWeatherRepository.csv  ← dataset (download from Kaggle)
└── README.md                    ← project documentation
```

---

## 📈 Progress

| Level | Topic | Status |
|---|---|---|
| 🟢 Level 1 | Data Loading & Exploration | ✅ Complete |
| 🟡 Level 2 | Pandas + NumPy Analysis | ✅ Complete |
| 🟠 Level 3 | Visualization | 🔄 In Progress |
| 🔴 Level 4 | Advanced Analysis | 🔄 Upcoming |

---

## 👩‍💻 Author

**Sakshee** — [@saksheex](https://github.com/saksheex)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
