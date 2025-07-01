n = 10  # binary: 1010

# Check if i-th bit is set
def is_set(n, i):
    return (n >> i) & 1

# Set i-th bit
def set_bit(n, i):
    return n | (1 << i)

# Clear i-th bit
def clear_bit(n, i):
    return n & ~(1 << i)

# Toggle i-th bit
def toggle_bit(n, i):
    return n ^ (1 << i)
