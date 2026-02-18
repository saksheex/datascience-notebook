import pandas as pd
df= pd.read_csv('student_lifestyle_performance_dataset.csv')
# A higher score indicates a student at high risk of burnout or low grades
df['Risk_Index'] = (df['Stress_Level_1_to_10'] / 10) - \
                   (df['Attendance_Percentage'] / 100) - \
                   (df['Sleep_Hours'] / 10)

# Display the 5 students most in need of a "break"
at_risk = df.sort_values(by='Risk_Index', ascending=False).head()
print(at_risk[['Branch', 'CGPA', 'Stress_Level_1_to_10', 'Risk_Index']])