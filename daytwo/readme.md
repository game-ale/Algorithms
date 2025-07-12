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

````
def query_2d_sum(prefix, r1, c1, r2, c2):
    return prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]

```
