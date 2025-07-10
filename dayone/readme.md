**Template using Euclid’s Algorithm (Recursive): **
```
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

    ```
**Template using Euclid’s Algorithm (Iterative):**
```
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    ```
    