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


numbers = np.array([1, 4, 9, 16, 25, 36])

sqrt = np.sqrt(numbers)

print(sqrt)

numbers2 = np.arange(1, 7) * 10

add = np.add(numbers, numbers2)
print(add)

multiply = np.multiply(numbers2, 5)
print(multiply)

numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2, 4, 6])

multiply2 = np.multiply(numbers3, numbers4)

print(multiply2)

"""This works because numbers4 has the same length as each row of numbers3,
so numpy can apply the multiply operation by treating numbers4 as if it were the following array:

array([[2,4,6],
[2,4,6]]"""

# Indexing and slicing

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

a = grades[0, 1]

# 96
print(a)

b = grades[1]
# Entire second row
print(b)

# To select sequential rows
first_two_row = grades[0:2]
print(first_two_row)

# To select multiple non seqeuntial rows
print(grades[[1, 3]])

# All rows and only first column
c = grades[:, 0]
print(c)

print()

# Select conscutive columns
d = grades[:, 1:3]
print(d)

print()
# Specific columns
e = grades[:, [0, 2]]

print(e)

print()
rand_grades = np.array(np.random.randint(60, 101, size=(12)))

grade_matrix = rand_grades.reshape(3, 4)
test_average = grade_matrix.mean(axis=0)
student_average = grade_matrix.mean(axis=1)

print(grade_matrix)
print(test_average)
print(student_average)

print()
# Shallow copies (view)
# The array method view returns the array object with a view of the original array

numbers = np.arange(1, 6)

numbers2 = numbers.view()

numbers[1] *= 10

print(numbers2)

numbers2[1] /= 10

# Impactd the original as well
print(numbers)

# Slice views
# Slices als create views
numbers2 = numbers[0:3]

numbers[1] *= 20

print(numbers2)
print()

# Deep copies
# The array method copy returns a new array object with a deep
# copy of the original copy

numbers = np.arange(1, 6)
numbers2 = numbers.copy()

numbers[1] *= 10

print(numbers)
print(numbers2)
print()
"""The array methods reshape and resize both enable you to change the array's dimensions
Method reshape returns a view (shallow copy) of the original array with the new dimensions. Does not modify the original array"""

grades = np.array([[87, 96, 70], [100, 87, 90]])

a = grades.reshape(1, 6)
print(a)
print(grades)
b = grades.resize(1, 6)

print(grades)
print()


# Method flatten deep copies th eoriginal array's data

flattened = grades.flatten()

# Ravel produces a view of the original array
# Which shares the grades array's data

raveled = grades.ravel()

# Confirm they share the same data
raveled[0] = 100
raveled[5] = 99

print(grades)
print()



# You can quickly transpose an array's rows and columns-that is"flip" the array,
# so the rows become the columns and the columns become rows
# the T attribute returns a transposed view of the array

transposed = grades.T
print(transposed)


# HStack
# Assume grades2 represents three additional exam grades for the
# two students in the grades array
grades = np.array([[87, 96, 70], [100, 87, 90]])

grades2 = np.array([[94,77,90],[100,81,82]])

# We can combine grades and grades2 with hstack
h_grades = np.hstack((grades,grades2))

print(h_grades)

# vstack
v_grades = np.vstack((grades,grades2))
print(v_grades)
