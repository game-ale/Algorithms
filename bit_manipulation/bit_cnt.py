"""🔎 2. Built-in Functions for Bit Counts
"""

t = n.bit_length()  # number of bits to represent n (excluding leading zeros)
y = bin(n).count('1')  # count set bits (1s)
n = 23  # binary: 10111
print(n.bit_length())     # Output: 5
print(bin(n).count('1'))  # Output: 4

