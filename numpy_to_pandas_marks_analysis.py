# Program: NumPy array to Pandas DataFrame conversion
# This program generates student marks using NumPy,
# converts them into a Pandas DataFrame,
# and calculates highest marks, average marks,
# and subject-wise statistics

import numpy as np
import pandas as pd

# Create NumPy array of student marks (5 students, 3 subjects)
marks_array = np.array([
    [85, 90, 78],
    [88, 76, 92],
    [70, 80, 85],
    [95, 89, 93],
    [60, 75, 70]
])

# Convert NumPy array into Pandas DataFrame
df = pd.DataFrame(marks_array, columns=["Math", "Science", "English"])

# Display DataFrame
print("\nStudent Marks DataFrame:\n")
print(df)

# Highest marks in each subject
print("\nHighest Marks (Subject-wise):")
print(df.max())

# Average marks in each subject
print("\nAverage Marks (Subject-wise):")
print(df.mean())

# Overall highest mark
overall_highest = df.values.max()

print("\nOverall Highest Marks:", overall_highest)

'''output::
Student Marks DataFrame:

   Math  Science  English
0    85       90       78
1    88       76       92
2    70       80       85
3    95       89       93
4    60       75       70

Highest Marks (Subject-wise):
Math         95
Science      90
English      93
dtype: int64

Average Marks (Subject-wise):
Math         82.0
Science      82.0
English      82.0
dtype: float64

Overall Highest Marks: 95
'''