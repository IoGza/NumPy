import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# ROWS - grades for each students
# COLS - grades for each student

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

# Calculates the mean based on the axis
# Doing it by column for every row
g = grades.mean(axis=0)
print("Average of each test", g)

# Doing it by row
h = grades.mean(axis=1)
print("Average of each student", h)
