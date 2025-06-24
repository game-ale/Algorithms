
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

***🧮 Digit DP – Summary & Purpose***

**Digit DP** is a dynamic programming technique used to **count or build numbers based on their digits**, especially when working with **very large numbers** (e.g., up to `10^18`).

---

## 🎯 Purpose

To **efficiently solve digit-related problems** in a range `[L, R]` **without checking every number one by one**.

✅ Perfect for problems where:
- You need to count how many numbers satisfy a digit-based condition.
- Brute force is too slow due to large input size.

---

## 🧠 Core Idea (Easy to Memorize)

> ⚙️ Build the number **digit by digit** (from left to right)  
> 🧩 At each step, track essential states and make decisions.

### 👇 While building the number, keep track of:
- 🔒 `tight`: Are we still bound to the upper limit digit?
- 0️⃣ `leading_zero`: Are we still dealing with leading zeros?
- 📦 `state`: A value or set storing info like:
  - Digits used so far
  - Sum of digits
  - Remainder/mod value
  - Anything your problem needs

### 💾 Use Memoization:
- Store results of solved subproblems to **avoid recomputation**.
- Usually implemented as a multidimensional `dp` array.

---

## ✨ Template Summary

```python
def digit_dp(pos, tight, leading_zero, state):
    if pos == len(digits):
        return 1 if is_valid(state) else 0

    if memo[pos][tight][leading_zero][state] is not None:
        return memo value

    limit = digits[pos] if tight else 9
    total = 0
    for d in range(0, limit + 1):
        new_tight = tight and (d == limit)
        new_state = update_state(state, d)
        total += digit_dp(pos + 1, new_tight, updated_leading_zero, new_state)

    memo[...] = total
    return total

