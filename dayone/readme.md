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
**Full Example for GCD, LCM, and Sieve Together**
```
import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

# Test examples
print("GCD of 12 and 15:", gcd(12, 15))
print("LCM of 12 and 15:", lcm(12, 15))
print("Primes up to 50:", sieve(50))

```
