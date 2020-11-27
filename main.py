import time
import random
import numpy as np




start = time.perf_counter()

# Creating array object
arr = np.array([[1, 2, 3],
                [4, 2, 5]])

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

end = time.perf_counter()
elapsed_numpy = end - start
print(f"elapsed time is {elapsed_numpy}")

"""
limit = 10000
nums = []

start = time.perf_counter()

for x in range(limit):
    nums.append(random.randint(0, limit))

min = limit + 1
for num in nums:
    if num < min:
        min = num
end = time.perf_counter()
elapsed = end - start
print(f"elapsed time for python {elapsed}")
print(min)

########## NumPy ##########



#nums = np.random.randint(0, limit, limit)
#min = nums.min()
#print(min)
"""
