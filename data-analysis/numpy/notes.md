# NumPy — Complete Notes

## What is NumPy and Why Use It?
- NumPy = Numerical Python, a library for fast numerical computations
- 10-50x faster than Python lists for numerical operations (written in C internally)
- Memory efficient: all elements in an array must be the same type
- Supports vectorized operations: apply an operation to an entire array at once, no loops needed
- Handles multidimensional data (2D tables, 3D image data, etc.)

## Creating Arrays
```python
import numpy as np

arr = np.array([1, 2, 3])
zeros = np.zeros(10)
ones = np.ones((3,3))
```

## List vs NumPy Array
- Python list: elements can be mixed types, slow for math operations
- NumPy array: elements must be the same type, fast for math operations
```python
list_result = [x * 2 for x in [1,2,3]]   # loop needed
arr_result = np.array([1,2,3]) * 2       # no loop needed
```

## Multidimensional Arrays
- **1D**: `[1,2,3]` — a simple list, one direction
- **2D (matrix)**: `[[1,2,3],[4,5,6]]` — rows and columns, like a table
- **3D**: `[[[1,2],[3,4]],[[5,6],[7,8]]]` — multiple 2D blocks stacked together

**Rule:** All lists at the same nesting level must have the same length, otherwise NumPy raises an error or creates a slow `dtype=object` array.

## shape and ndim
- **shape**: size of the array at each level, e.g. `(2,3)` = 2 rows, 3 columns
- **ndim**: number of dimensions/nesting levels
- Trick: number of values in `shape` = `ndim`
```python
arr.shape
arr.ndim
```

## dtype (Data Type)
- Every NumPy array has one fixed dtype — all elements must match
- Common dtypes: `int64`, `float64`, `bool`, `object`
```python
arr.dtype
arr = np.array([1,2,3], dtype=np.float64)
```
- Mixing int and float in a list makes NumPy upgrade everything to float

## Matrix Multiplication
- `*` = element-wise multiplication (each position multiplied separately)
- `@` or `np.matmul()` = proper matrix multiplication (row × column sum)
```python
a @ b
np.matmul(a, b)   # same result as @
```

## np.concatenate()
- Joins multiple arrays into one; arrays passed as a tuple
```python
np.concatenate((arr1, arr2), axis=0)   # joins along rows (vertical)
np.concatenate((arr1, arr2), axis=1)   # joins along columns (horizontal)
```
- Same axis rule applies to `.sum(axis=0)` / `.sum(axis=1)` etc.

## np.reshape()
- Changes shape without changing data; total elements must stay the same
```python
arr.reshape(2, 3)
arr.reshape(2, -1)   # -1 lets NumPy calculate that dimension automatically
```

## Indexing (single element)
```python
arr = np.array([10, 20, 30, 40, 50])
arr[0]      # 10 (first)
arr[-1]     # 50 (last)
```
- Indexing starts at 0; negative indices count from the end

## Slicing (range of elements) — `arr[start:stop:step]`
```python
arr[1:4]    # index 1,2,3 (stop excluded)
arr[:3]     # start to index 2
arr[2:]     # index 2 to end
arr[::2]    # every 2nd element
arr[::-1]   # reversed
```

## 2D Indexing/Slicing — `arr[row, col]`
```python
arr2d[0, 1]      # row 0, column 1
arr2d[1]         # entire row 1
arr2d[:, 1]      # entire column 1
arr2d[0:2, 0:2]  # top-left 2x2 block
```

## Boolean Indexing (filtering)
```python
arr[arr > 20]
arr[arr % 2 == 0]
```

## Fancy Indexing
```python
arr[[0, 2, 4]]   # elements at specific positions
```

## Counting Matches with Boolean + sum()
- `True` = 1, `False` = 0 in arithmetic
```python
(actual == predicted).sum()   # counts matching positions
```

## Important: Slicing Returns a View, Not a Copy
```python
sliced = arr[1:3]
sliced[0] = 999                 # modifies the ORIGINAL array too
sliced_copy = arr[1:3].copy()   # independent copy
```

## Statistics & Aggregation
```python
arr.mean(), arr.std(), arr.sum(), arr.max(), arr.min()
np.median(arr)
np.argmax(arr)   # index of max value
np.argmin(arr)   # index of min value
np.unique(arr)                        # unique values
np.unique(arr, return_counts=True)    # unique values + counts
```

## Generating Ranges
```python
np.arange(0, 10, 2)      # start, stop (excluded), step
np.linspace(0, 1, 5)     # start, stop (included), number of points
```

## Stacking
```python
np.vstack((a, b))   # stack vertically (rows)
np.hstack((a, b))   # stack horizontally (columns)
```

## Reshaping Helpers
```python
arr.flatten()   # collapse to 1D
arr.T           # transpose (flip rows/columns)
```

## Linear Algebra
```python
np.linalg.inv(matrix)     # matrix inverse
np.linalg.det(matrix)     # determinant
np.linalg.norm(vector)    # vector magnitude
np.dot(a, b)              # dot product
```

## Conditional Operations
```python
np.where(arr > 5, 1, 0)   # replace values based on condition
np.clip(arr, 0, 10)       # limit values to a range
```

## Reproducibility
```python
np.random.seed(42)   # same random numbers every run
```

## File I/O
```python
np.genfromtxt('file.csv', delimiter=',', skip_header=1)   # load CSV into array
np.savetxt('output.txt', arr, delimiter=',', fmt='%d')     # save array to file
```
- In MLP, Pandas (`pd.read_csv()` / `df.to_csv()`) is used more often for this than NumPy

## urllib (brief)
- Built-in Python library for downloading files from a URL
```python
import urllib.request
urllib.request.urlretrieve('https://...file.csv', 'file.csv')
```

## Vector Operations
```python
a + b                          # vector addition
np.dot(a, b)                   # dot product

# Euclidean distance
np.sqrt(np.sum((a - b)**2))
# or
np.linalg.norm(a - b)

# Cosine similarity
np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

## More Statistics
```python
np.var(arr)                    # variance
np.percentile(arr, 50)         # 50th percentile (median)
np.corrcoef(a, b)              # correlation matrix
np.cov(a, b)                   # covariance matrix

# Z-score (standardization)
z = (arr - arr.mean()) / arr.std()
```

## Distance Matrix (pairwise distances between points)
```python
from scipy.spatial.distance import cdist
cdist(points_A, points_B)      # matrix of distances between every pair

# or manually for two vectors:
np.linalg.norm(a - b)
```

## Images as NumPy Arrays
- A color image is a 3D array: (height, width, 3) — the 3 is for RGB channels
```python
image.shape           # e.g. (100, 100, 3)
image.flatten()       # collapse image to 1D array

# RGB to Grayscale (weighted average of R, G, B channels)
gray = 0.2989*image[:,:,0] + 0.5870*image[:,:,1] + 0.1140*image[:,:,2]
```