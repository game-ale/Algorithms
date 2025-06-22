
**Lazy Prim's MST Cheat Sheet**
1. Core Idea (Remember This!)
"Grow a tree by always picking the smallest edge touching it."

2. 3 Key Components to Memorize
Min-Heap → Stores edges ((weight, u, v))

Visited Set → Tracks nodes already in MST

MST Edges → Stores the result

Mnemonic Shortcuts
"HVM" → Heap + Visited + MST

"Pick, Skip, Grow" →

Pick smallest edge from heap.

Skip if node is visited.

Grow MST by adding edges.

#Common Pitfalls
Forget to skip visited nodes → Infinite loop.

Heap stores duplicates → Safe but inefficient.

When to Use Lazy Prim?
Sparse graphs (few edges).

Coding interviews (easier to implement than eager).

# 📘 DP + Bitmasking: Core Operations

This document summarizes key bitmask operations commonly used in dynamic programming (DP), especially in problems involving subsets, permutations, or combinatorial optimization.

---

## 🧮 Core Bitmask Operations

| **Operation**               | **Description**                                            | **Python Example**                 |
|----------------------------|------------------------------------------------------------|------------------------------------|
| Check if bit is ON         | Test if `i`-th bit is set in `mask`                        | `(mask >> i) & 1`                  |
| Turn ON a bit              | Set the `i`-th bit to 1                                    | `mask | (1 << i)`                  |
| Turn OFF a bit             | Set the `i`-th bit to 0                                    | `mask & ~(1 << i)`                 |
| Toggle a bit               | Flip the `i`-th bit                                        | `mask ^ (1 << i)`                  |
| Check if subset A ⊆ B      | Check if all bits in `A` are present in `B`                | `(A & B) == A`                     |
| Set all bits               | Set all `n` bits to 1                                      | `(1 << n) - 1`                     |
| Count ON bits (popcount)   | Count number of 1s in the bitmask                          | `bin(mask).count('1')` or `mask.bit_count()` |
| Generate all subsets       | Iterate through all submasks of a mask                     | See code snippet below             |
| Next state mask            | Move to a new state by turning ON a bit                    | `next_mask = mask | (1 << j)`     |
| Bitmask iteration          | Loop through all masks from `0` to `2ⁿ - 1`                | `for mask in range(1 << n):`       |
| Bitmask as DP state        | Represent a visited/assigned state                         | `dp[mask][u] = ...`                |
| Subset iteration           | Generate all subsets of a given bitmask                    | `sub = mask; while sub: ...`       |

---

## 🔁 Subset Iteration Snippet

```python
mask = 0b1011  # Example mask
sub = mask
while sub:
    print(bin(sub))
    sub = (sub - 1) & mask
