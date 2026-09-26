# NumPy — Complete Notes

## 1. What is NumPy and Why Use It?
- NumPy = Numerical Python, a library for fast numerical computations
- 10-50x faster than Python lists for numerical operations, because it's written in C internally
- Memory efficient: all elements in an array must be the same type (unlike Python lists, which can mix types)
- Supports vectorized operations: apply an operation to an entire array at once, without writing a loop
- Handles multidimensional data naturally — 2D tables, 3D image data, etc.

## 2. Creating Arrays
```python
import numpy as np

arr = np.array([1, 2, 3])   # basic array from a list
zeros = np.zeros(10)         # array of 10 zeros
ones = np.ones((3,3))        # 3x3 array of ones
full = np.full((3,3), 7)     # 3x3 array filled entirely with 7
arange = np.arange(0, 10, 2) # [0,2,4,6,8] - start, stop (excluded), step
lin = np.linspace(0, 1, 5)   # 5 evenly spaced points between 0 and 1 (inclusive)
```

## 3. List vs NumPy Array
- Python list: elements can be mixed types, math operations require a manual loop, slower
- NumPy array: elements must be the same type, math operations apply directly to the whole array, much faster
```python
list_result = [x * 2 for x in [1,2,3]]   # loop needed for a list
arr_result = np.array([1,2,3]) * 2       # no loop needed for an array
```

## 4. Inspecting an Array
```python
arr.shape     # size at each dimension, e.g. (2,3) = 2 rows, 3 columns
arr.ndim      # number of dimensions (1D, 2D, 3D, etc.)
arr.dtype     # data type of the elements (int64, float64, etc.)
arr.size      # total number of elements in the array
```
- Trick: the number of values inside `shape` tells you the `ndim`

## 5. Multidimensional Arrays
- **1D array**: `[1,2,3]` — a simple list, one direction
- **2D array (matrix)**: `[[1,2,3],[4,5,6]]` — rows and columns, like a table
- **3D array**: `[[[1,2],[3,4]],[[5,6],[7,8]]]` — multiple 2D blocks stacked together

**Rule:** every list at the same nesting level must have the same length. If they don't, NumPy either throws an error or silently creates a slow `dtype=object` array (losing all the speed benefits).

## 6. dtype (Data Type)
- Every NumPy array has one fixed dtype shared by all elements
- Common dtypes: `int64`, `float64`, `bool`, `object`
```python
arr.dtype
arr = np.array([1,2,3], dtype=np.float64)   # set the type explicitly
```
- If a list mixes int and float values, NumPy automatically upgrades the whole array to float, so no data is lost

## 7. Indexing (Accessing a Single Element)
```python
arr = np.array([10, 20, 30, 40, 50])
arr[0]      # 10 -> first element
arr[-1]     # 50 -> last element
```
- Indexing starts at 0
- Negative indices count backward from the end (-1 is the last element)

## 8. Slicing (Accessing a Range of Elements)
Syntax: `arr[start:stop:step]` — the `stop` index is always excluded from the result
```python
arr[1:4]    # elements at index 1,2,3 (index 4 is NOT included)
arr[:3]     # from the start up to index 2
arr[2:]     # from index 2 to the end
arr[::2]    # every 2nd element
arr[::-1]   # the whole array reversed
```

## 9. 2D Indexing/Slicing — `arr[row, col]`
```python
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr2d[0, 1]      # row 0, column 1 -> single value
arr2d[1]         # entire row 1
arr2d[:, 1]      # entire column 1 (all rows, column 1)
arr2d[0:2, 0:2]  # top-left 2x2 sub-block
```

## 10. Boolean Indexing (Filtering by Condition)
```python
arr[arr > 20]        # keeps only elements greater than 20
arr[arr % 2 == 0]    # keeps only even numbers
```
This works because the condition (`arr > 20`) creates a True/False array of the same shape, and NumPy uses that to select matching elements.

## 11. Fancy Indexing
```python
arr[[0, 2, 4]]   # pulls out elements at index positions 0, 2, and 4 in one go
```

## 12. Counting Matches with Boolean + sum()
In arithmetic, `True` behaves as `1` and `False` as `0`. This is useful for counting how many values match between two arrays.
```python
(actual == predicted).sum()   # counts how many positions are equal
```

## 13. Important Trap: Slicing Returns a View, Not a Copy
A slice doesn't create new data — it points back to the same memory as the original array. So modifying a slice modifies the original too.
```python
arr = np.array([1, 2, 3, 4, 5])
sliced = arr[1:3]
sliced[0] = 999
print(arr)   # [1, 999, 3, 4, 5] -> original changed too!

sliced_copy = arr[1:3].copy()   # this creates an independent copy instead
```

## 14. Matrix Multiplication
- `*` performs element-wise multiplication (each position multiplied separately)
- `@` or `np.matmul()` performs true matrix multiplication (row × column sums), which is what "multiplying matrices" means in linear algebra
```python
a * b               # element-wise
a @ b                # matrix multiplication
np.matmul(a, b)      # same result as @, just a full function name instead of a symbol
```

## 15. Linear Algebra
```python
np.linalg.inv(matrix)     # inverse of a matrix
np.linalg.det(matrix)     # determinant of a matrix
np.linalg.norm(vector)    # magnitude/length of a vector
np.dot(a, b)                # dot product of two vectors
```

## 16. Statistics & Aggregation
```python
arr.mean()      # average
arr.std()       # standard deviation
arr.var()       # variance
arr.sum()       # total
arr.max()       # largest value
arr.min()       # smallest value
np.median(arr)              # middle value
np.percentile(arr, 50)      # value at the 50th percentile (same as median)
np.argmax(arr)              # index of the largest value
np.argmin(arr)              # index of the smallest value
np.unique(arr)                       # list of unique values
np.unique(arr, return_counts=True)   # unique values plus how many times each appears
np.corrcoef(a, b)   # correlation matrix between a and b
np.cov(a, b)          # covariance matrix between a and b
z = (arr - arr.mean()) / arr.std()   # z-score: how many std-deviations away from the mean
```

## 17. Vector Operations
```python
a + b   # vector addition (element-wise sum)

# Euclidean distance: straight-line distance between two points/vectors
np.sqrt(np.sum((a - b)**2))
np.linalg.norm(a - b)      # same result, shorter way to write it

# Cosine similarity: how similar the direction of two vectors is (1 = identical direction)
np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

## 18. Reshaping an Array
Changes the array's structure without changing its data. The total number of elements must stay the same — e.g. 6 elements can become 2×3 or 3×2, but not 2×4.
```python
arr.reshape(2, 3)
arr.reshape(2, -1)   # -1 tells NumPy to work out that dimension automatically
```

## 19. Other Reshaping Helpers
```python
arr.flatten()   # collapses any multidimensional array down to 1D
arr.T             # transpose: flips rows and columns
```

## 20. Combining Arrays
```python
np.concatenate((a, b), axis=0)   # joins along rows (stacks vertically) — arrays passed as a tuple
np.concatenate((a, b), axis=1)   # joins along columns (stacks side by side)
np.vstack((a, b))                   # shortcut for vertical stacking
np.hstack((a, b))                   # shortcut for horizontal stacking
```
The same `axis` rule (0 = rows, 1 = columns) applies to functions like `.sum(axis=0)` too.

## 21. Conditional Operations
```python
np.where(arr > 5, 1, 0)   # replaces each value: 1 if condition is true, 0 otherwise
np.clip(arr, 0, 10)         # forces all values into the range [0, 10]
```

## 22. Reproducibility
```python
np.random.seed(42)   # fixes the randomness, so random operations give the same result every run
```

## 23. File I/O
```python
np.genfromtxt('file.csv', delimiter=',', skip_header=1)   # loads a CSV into an array, skipping the header row
np.savetxt('output.txt', arr, delimiter=',', fmt='%d')      # saves an array to a text file
```
- In MLP, Pandas (`pd.read_csv()` / `df.to_csv()`) is used far more often than NumPy for this — this is mainly good to know it exists

## 24. urllib (brief mention)
Built-in Python library (not NumPy) used to download files directly from a URL.
```python
import urllib.request
urllib.request.urlretrieve('https://...file.csv', 'file.csv')
```

## 25. Images as NumPy Arrays
A color image is stored as a 3D array: (height, width, 3), where the 3 represents the Red, Green, and Blue channels.
```python
image.shape       # e.g. (100, 100, 3)
image.flatten()   # collapses the image into a 1D array

# Convert to grayscale using a weighted average of the three channels
gray = 0.2989*image[:,:,0] + 0.5870*image[:,:,1] + 0.1140*image[:,:,2]
```

## 26. Distance Matrix (Pairwise Distances)
Used when you need the distance between every pair of points in two sets, not just two single vectors.
```python
from scipy.spatial.distance import cdist
cdist(points_A, points_B)   # returns a matrix of distances between every pair
```# NumPy — Complete Notes

## 1. What is NumPy and Why Use It?
- NumPy = Numerical Python, a library for fast numerical computations
- 10-50x faster than Python lists for numerical operations, because it's written in C internally
- Memory efficient: all elements in an array must be the same type (unlike Python lists, which can mix types)
- Supports vectorized operations: apply an operation to an entire array at once, without writing a loop
- Handles multidimensional data naturally — 2D tables, 3D image data, etc.

## 2. Creating Arrays
```python
import numpy as np

arr = np.array([1, 2, 3])   # basic array from a list
zeros = np.zeros(10)         # array of 10 zeros
ones = np.ones((3,3))        # 3x3 array of ones
full = np.full((3,3), 7)     # 3x3 array filled entirely with 7
arange = np.arange(0, 10, 2) # [0,2,4,6,8] - start, stop (excluded), step
lin = np.linspace(0, 1, 5)   # 5 evenly spaced points between 0 and 1 (inclusive)
```

## 3. List vs NumPy Array
- Python list: elements can be mixed types, math operations require a manual loop, slower
- NumPy array: elements must be the same type, math operations apply directly to the whole array, much faster
```python
list_result = [x * 2 for x in [1,2,3]]   # loop needed for a list
arr_result = np.array([1,2,3]) * 2       # no loop needed for an array
```

## 4. Inspecting an Array
```python
arr.shape     # size at each dimension, e.g. (2,3) = 2 rows, 3 columns
arr.ndim      # number of dimensions (1D, 2D, 3D, etc.)
arr.dtype     # data type of the elements (int64, float64, etc.)
arr.size      # total number of elements in the array
```
- Trick: the number of values inside `shape` tells you the `ndim`

## 5. Multidimensional Arrays
- **1D array**: `[1,2,3]` — a simple list, one direction
- **2D array (matrix)**: `[[1,2,3],[4,5,6]]` — rows and columns, like a table
- **3D array**: `[[[1,2],[3,4]],[[5,6],[7,8]]]` — multiple 2D blocks stacked together

**Rule:** every list at the same nesting level must have the same length. If they don't, NumPy either throws an error or silently creates a slow `dtype=object` array (losing all the speed benefits).

## 6. dtype (Data Type)
- Every NumPy array has one fixed dtype shared by all elements
- Common dtypes: `int64`, `float64`, `bool`, `object`
```python
arr.dtype
arr = np.array([1,2,3], dtype=np.float64)   # set the type explicitly
```
- If a list mixes int and float values, NumPy automatically upgrades the whole array to float, so no data is lost

## 7. Indexing (Accessing a Single Element)
```python
arr = np.array([10, 20, 30, 40, 50])
arr[0]      # 10 -> first element
arr[-1]     # 50 -> last element
```
- Indexing starts at 0
- Negative indices count backward from the end (-1 is the last element)

## 8. Slicing (Accessing a Range of Elements)
Syntax: `arr[start:stop:step]` — the `stop` index is always excluded from the result
```python
arr[1:4]    # elements at index 1,2,3 (index 4 is NOT included)
arr[:3]     # from the start up to index 2
arr[2:]     # from index 2 to the end
arr[::2]    # every 2nd element
arr[::-1]   # the whole array reversed
```

## 9. 2D Indexing/Slicing — `arr[row, col]`
```python
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr2d[0, 1]      # row 0, column 1 -> single value
arr2d[1]         # entire row 1
arr2d[:, 1]      # entire column 1 (all rows, column 1)
arr2d[0:2, 0:2]  # top-left 2x2 sub-block
```

## 10. Boolean Indexing (Filtering by Condition)
```python
arr[arr > 20]        # keeps only elements greater than 20
arr[arr % 2 == 0]    # keeps only even numbers
```
This works because the condition (`arr > 20`) creates a True/False array of the same shape, and NumPy uses that to select matching elements.

## 11. Fancy Indexing
```python
arr[[0, 2, 4]]   # pulls out elements at index positions 0, 2, and 4 in one go
```

## 12. Counting Matches with Boolean + sum()
In arithmetic, `True` behaves as `1` and `False` as `0`. This is useful for counting how many values match between two arrays.
```python
(actual == predicted).sum()   # counts how many positions are equal
```

## 13. Important Trap: Slicing Returns a View, Not a Copy
A slice doesn't create new data — it points back to the same memory as the original array. So modifying a slice modifies the original too.
```python
arr = np.array([1, 2, 3, 4, 5])
sliced = arr[1:3]
sliced[0] = 999
print(arr)   # [1, 999, 3, 4, 5] -> original changed too!

sliced_copy = arr[1:3].copy()   # this creates an independent copy instead
```

## 14. Matrix Multiplication
- `*` performs element-wise multiplication (each position multiplied separately)
- `@` or `np.matmul()` performs true matrix multiplication (row × column sums), which is what "multiplying matrices" means in linear algebra
```python
a * b               # element-wise
a @ b                # matrix multiplication
np.matmul(a, b)      # same result as @, just a full function name instead of a symbol
```

## 15. Linear Algebra
```python
np.linalg.inv(matrix)     # inverse of a matrix
np.linalg.det(matrix)     # determinant of a matrix
np.linalg.norm(vector)    # magnitude/length of a vector
np.dot(a, b)                # dot product of two vectors
```

## 16. Statistics & Aggregation
```python
arr.mean()      # average
arr.std()       # standard deviation
arr.var()       # variance
arr.sum()       # total
arr.max()       # largest value
arr.min()       # smallest value
np.median(arr)              # middle value
np.percentile(arr, 50)      # value at the 50th percentile (same as median)
np.argmax(arr)              # index of the largest value
np.argmin(arr)              # index of the smallest value
np.unique(arr)                       # list of unique values
np.unique(arr, return_counts=True)   # unique values plus how many times each appears
np.corrcoef(a, b)   # correlation matrix between a and b
np.cov(a, b)          # covariance matrix between a and b
z = (arr - arr.mean()) / arr.std()   # z-score: how many std-deviations away from the mean
```

## 17. Vector Operations
```python
a + b   # vector addition (element-wise sum)

# Euclidean distance: straight-line distance between two points/vectors
np.sqrt(np.sum((a - b)**2))
np.linalg.norm(a - b)      # same result, shorter way to write it

# Cosine similarity: how similar the direction of two vectors is (1 = identical direction)
np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

## 18. Reshaping an Array
Changes the array's structure without changing its data. The total number of elements must stay the same — e.g. 6 elements can become 2×3 or 3×2, but not 2×4.
```python
arr.reshape(2, 3)
arr.reshape(2, -1)   # -1 tells NumPy to work out that dimension automatically
```

## 19. Other Reshaping Helpers
```python
arr.flatten()   # collapses any multidimensional array down to 1D
arr.T             # transpose: flips rows and columns
```

## 20. Combining Arrays
```python
np.concatenate((a, b), axis=0)   # joins along rows (stacks vertically) — arrays passed as a tuple
np.concatenate((a, b), axis=1)   # joins along columns (stacks side by side)
np.vstack((a, b))                   # shortcut for vertical stacking
np.hstack((a, b))                   # shortcut for horizontal stacking
```
The same `axis` rule (0 = rows, 1 = columns) applies to functions like `.sum(axis=0)` too.

## 21. Conditional Operations
```python
np.where(arr > 5, 1, 0)   # replaces each value: 1 if condition is true, 0 otherwise
np.clip(arr, 0, 10)         # forces all values into the range [0, 10]
```

## 22. Reproducibility
```python
np.random.seed(42)   # fixes the randomness, so random operations give the same result every run
```

## 23. File I/O
```python
np.genfromtxt('file.csv', delimiter=',', skip_header=1)   # loads a CSV into an array, skipping the header row
np.savetxt('output.txt', arr, delimiter=',', fmt='%d')      # saves an array to a text file
```
- In MLP, Pandas (`pd.read_csv()` / `df.to_csv()`) is used far more often than NumPy for this — this is mainly good to know it exists

## 24. urllib (brief mention)
Built-in Python library (not NumPy) used to download files directly from a URL.
```python
import urllib.request
urllib.request.urlretrieve('https://...file.csv', 'file.csv')
```

## 25. Images as NumPy Arrays
A color image is stored as a 3D array: (height, width, 3), where the 3 represents the Red, Green, and Blue channels.
```python
image.shape       # e.g. (100, 100, 3)
image.flatten()   # collapses the image into a 1D array

# Convert to grayscale using a weighted average of the three channels
gray = 0.2989*image[:,:,0] + 0.5870*image[:,:,1] + 0.1140*image[:,:,2]
```

## 26. Distance Matrix (Pairwise Distances)
Used when you need the distance between every pair of points in two sets, not just two single vectors.
```python
from scipy.spatial.distance import cdist
cdist(points_A, points_B)   # returns a matrix of distances between every pair
```