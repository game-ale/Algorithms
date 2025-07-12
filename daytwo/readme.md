**Sum Query [l, r]**
```
def query_sum(prefix, l, r):
    return prefix[r+1] - prefix[l]

```

**🚀 2D Prefix Sum (Matrix Prefix Sum)**
**Build 2D Prefix Sum**

```
def build_2d_prefix_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    prefix = [[0]*(cols+1) for _ in range(rows+1)]

    for i in range(1, rows+1):
        for j in range(1, cols+1):
            prefix[i][j] = matrix[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

    return prefix

```
***Sum Query for Submatrix [(r1,c1) to (r2,c2)]***

```
def query_2d_sum(prefix, r1, c1, r2, c2):
    return prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]

```
**⚙️ Difference Array (For Range Updates)**
**➤ 1. 1D Difference Array**

```
def build_diff_array(arr):
    n = len(arr)
    diff = [0] * (n + 1)
    for i in range(n):
        diff[i] = arr[i] - (arr[i-1] if i > 0 else 0)
    return diff

```

**Range increment (l to r): add val to all arr[l...r]**

```def range_update(diff, l, r, val):
    diff[l] += val
    if r + 1 < len(diff):
        diff[r+1] -= val

# Build back the array
def rebuild_from_diff(diff):
    n = len(diff)
    arr = [0] * n
    arr[0] = diff[0]
    for i in range(1, n):
        arr[i] = arr[i-1] + diff[i]
    return arr

```

***📊 Common Applications***
|------------------------------------------|----------------------------|
|Problem Type	                           | Solution Technique         |
|------------------------------------------|----------------------------|
|Range sum query (static array)	           | Prefix sum                 |
|Range sum query (frequent updates)        | Segment Tree / Fenwick Tree|
|Range add, range sum query	Difference     | Array + Prefix Sum         |
|2D range sum (static)	                   | 2D Prefix sum              |
|Find subarrays with a given sum	       | Prefix sum + Hash Map      |
|Counting problems (prefix sum of counts)  | Prefix sum                 |
|------------------------------------------|----------------------------|

***🔍 Variants***
**1. Prefix XOR**
```
prefix_xor = [0] * (n+1)
for i in range(n):
    prefix_xor[i+1] = prefix_xor[i] ^ arr[i]

```
**2. Prefix Min / Max**

```
prefix_min = [float('inf')] * n
prefix_min[0] = arr[0]
for i in range(1, n):
    prefix_min[i] = min(prefix_min[i-1], arr[i])
#🛠️ Python Libraries
itertools.accumulate():
from itertools import accumulate
prefix = list(accumulate(arr))

```
