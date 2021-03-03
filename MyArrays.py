import numpy as np


integers = np.array([1, 2, 3])

print(type(integers))
print(integers)


# One dimensional array from list comprehensio that
# produces even integers from 2 - 20

even = np.array([i for i in range(2, 21, 2)])
print(even)

multiIntegers = np.array([[1, 2, 3], [4, 5, 6]])
print(multiIntegers)


multiFLoats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(multiFLoats)