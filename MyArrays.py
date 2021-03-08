import numpy as np
import random


# integers = np.array([1, 2, 3])

# print(type(integers))
# print(integers)


# # One dimensional array from list comprehensio that
# # produces even integers from 2 - 20

# even = np.array([i for i in range(2, 21, 2)])
# print(even)

# integers = np.array([[1, 2, 3], [4, 5, 6]])
# print(integers)


# multiFLoats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
# print(multiFLoats)

# a = integers.dtype
# # Dimensions of
# b = integers.ndim
# # Shows the dimensions of the array
# c = integers.shape
# # Total number of elemenets in the whole array
# d = integers.size


# print()

# for row in integers:
#     print(type(row))
#     print(row)
#     for col in row:
#         # End = ' ' changes the default string end value from newline to a space
#         print(col, end = ' ')

# # Iterates through all values, disregarding columns and rows
# for i in integers.flat:
#     print(i)


print()
integers = np.array(
    [
        [random.randint(1, 10) for x in range(5)],
        [random.randint(1, 10) for x in range(5)],
    ]
)
print(integers)
print()

b = np.array(np.random.randint(1, 10, size=(2, 5)))
print(b)


# Create an array of 5 elements; default float type
c = np.zeros(5)

# create an array of 5 elemnets of 1s
print(np.ones(5))

print(np.ones((2, 4), dtype=int))

# Create an array of 3 rows of 5 columns of the number 13
print(np.full((3, 5), 13))

# Like the rand function, using integers
print(np.arange(5))

# Included lower limit of 5 but not upper limit 10
print(np.arange(5, 10))

# Step value for descending order
print(np.arange(10, 1, -2))

# Evenly spaced float range
print(np.linspace(0.0, 1.0, num=5))

array1 = np.arange(1, 21)

# Reshaoe method can change the dimension of an array
array2 = array1.reshape(4, 5)

print(array1)

print(array2)


array3 = np.arange(1, 100001).reshape(4, 25000)

print(array3)

array4 = np.arange(1, 100001).reshape(100, 1000)

print(array4)

numbers = np.arange(1, 6)

# Adds ten to each element in the array
numbers += 10

print(numbers)

# Broadcasting
print(numbers * 2)
# numbers * [2,2,2,2,2]

print(numbers ** 3)

print(numbers)


# Multiplying integer arrays with floating point arrays
numbers2 = np.linspace(1.1, 5.5, 5)
a = numbers * numbers2
print(a)

# comparing arrays
print(numbers >= 13)

print(numbers2 < numbers)

print(numbers ==numbers2)