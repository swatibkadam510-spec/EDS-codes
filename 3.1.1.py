import numpy as np

# write your code here...
# Input number of rows and columns
rows, cols = map(int, input().split())

# List to store elements
elements = []

# Input elements row-wise
for i in range(rows):
    row = list(map(int, input().split()))
    elements.extend(row)

# Create NumPy array and reshape
arr = np.array(elements).reshape(rows, cols)

# Display results
print(arr)

print(arr.ndim)
print( arr.shape)
print( arr.size)
